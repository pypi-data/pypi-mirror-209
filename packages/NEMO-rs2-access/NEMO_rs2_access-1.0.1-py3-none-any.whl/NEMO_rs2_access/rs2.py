import datetime
from logging import getLogger
from typing import Dict, List, Set, Type, Union

import requests
from NEMO.exceptions import NEMOException
from NEMO.models import Area, AreaAccessRecord, Customization, UsageEvent, User
from NEMO.utilities import beginning_of_the_day, distinct_qs_value_list
from NEMO.views.calendar import shorten_reservation
from django.conf import settings
from django.db.models import Model
from django.http import HttpResponseBadRequest
from django.utils import timezone
from requests.auth import HTTPBasicAuth

from NEMO_rs2_access.models import Reader

rs2_logger = getLogger(__name__)

NEXT_EVENTS_BEGIN_DATE = "rs2_event_begin_date"
RELEVANT_MESSAGE_TYPES = [0]  # 0 is the event message type
RELEVANT_EVENT_TYPES = [601, 607]  # 601 is access granted, 607 Access Granted Door Unlocked

READERS_URL = "/Readers"
READERS_HISTORY_URL = "/Readers/{}/EventHistory?beginDate={}"

reader_mapping = {
    "reader_name": "ReaderName",
    "site_id": "SiteID",
    "installed": "DeviceInstalled",
}


def sync_access():
    try:
        # default date is beginning of the day today if not set in Customization
        default_date = beginning_of_the_day(datetime.datetime.now(), in_local_timezone=False).isoformat()
        last_event_date_read, created = Customization.objects.get_or_create(
            name=NEXT_EVENTS_BEGIN_DATE, defaults={"value": default_date}
        )
        next_event_date = last_event_date_read.value
        events, readers = get_sorted_reader_events(next_event_date)
        try:
            for event in events:
                reader_id = event["SourceId"]
                badge_number_field = event[settings.RS2_BADGE_NUMBER_SYNC_FIELD]
                event_time = event["EventDateObject"]
                reader = readers.get(reader_id)
                area = reader.area
                if area:
                    event_user = event.get("Cardholder")
                    user = User.objects.filter(badge_number=badge_number_field).first()
                    if user:
                        login_logout(user, reader, event_time)
                    else:
                        rs2_logger.error(
                            f"No NEMO matching user found for {settings.RS2_BADGE_NUMBER_SYNC_FIELD} {badge_number_field} - {event_user} (event at location {reader.reader_name})"
                        )
                # Only set next sequence number when we are done with the current event
                next_event_date = event["EventDate"]
        finally:
            last_event_date_read.value = next_event_date
            last_event_date_read.save()
    except Customization.DoesNotExist:
        message = (
            f"No last sequence number was set in Customization. Please add one with the name '{NEXT_EVENTS_BEGIN_DATE}'"
        )
        rs2_logger.error(message)
        raise NEMOException(msg=message)
    except:
        rs2_logger.exception("There was an error communication with the RS2 access system")


def get_sorted_reader_events(begin_date: str) -> (List[Dict], Dict[int, Reader]):
    """
    Get events for all relevant readers
    Then merge them all (since login-logout happen in different readers)
    Finally we need to sort them all to recreate the chronological order of things
    """
    reader_ids = Reader.objects.filter(area__isnull=False).values_list("reader_id", flat=True)
    readers = Reader.objects.in_bulk(id_list=reader_ids, field_name="reader_id")
    events = []
    for reader_id in readers:
        response = request_get(READERS_HISTORY_URL.format(reader_id, begin_date))
        response.raise_for_status()
        reader_events = response.json()
        for reader_event in reader_events:
            if reader_event["EventType"] in RELEVANT_EVENT_TYPES:
                reader_event["SourceId"] = reader_id
                reader_event["EventDateObject"] = datetime.datetime.fromisoformat(
                    reader_event["EventDate"]
                ).astimezone()
                events.append(reader_event)
    events.sort(key=lambda x: x["EventDateObject"])
    return events, readers


def sync_readers():
    sync_model_rest(READERS_URL, Reader, "ReaderID", reader_mapping)


def sync_model_rest(url, model_class: Type[Model], remote_id_field_name: str, mapping: Dict):
    sync_model_rest_data(request_get(url).json(), model_class, remote_id_field_name, mapping)


def sync_model_rest_data(data, model_class: Type[Model], remote_id_field_name: str, mapping: Dict):
    model_id_field = f"{model_class._meta.model_name}_id"
    try:
        db_data_ids = distinct_qs_value_list(model_class.objects.all(), model_id_field)
        remote_data_ids = set()
        for item in data:
            item_id = item.get(remote_id_field_name)
            remote_data_ids.add(item_id)
            defaults = {model_field: item.get(remote_field) for model_field, remote_field in mapping.items()}
            defaults["data"] = item
            model_class.objects.update_or_create(**{model_id_field: item_id}, defaults=defaults)
        to_remove = db_data_ids.difference(remote_data_ids)
        model_class.objects.filter(**{f"{model_id_field}__in": to_remove}).delete()
        if to_remove:
            rs2_logger.info(f"Deleted {model_class} with ids: {', '.join(str(x) for x in to_remove)}")
    except:
        rs2_logger.exception(f"Error syncing {model_class} table")


def request_get(url_suffix: str):
    rs2_settings = settings.RS2_ACCESS
    if rs2_settings:
        auth = (
            HTTPBasicAuth(rs2_settings["auth"].get("user_id"), rs2_settings["auth"].get("password"))
            if "auth" in rs2_settings
            else None
        )
        headers = {"PublicKey": rs2_settings.get("public_key")}
        timeout = rs2_settings.get("timeout", 30)
        return requests.get(rs2_settings.get("url") + url_suffix, auth=auth, headers=headers, timeout=timeout)
    else:
        return HttpResponseBadRequest("no RS2_ACCESS settings found, please add them to your settings.py")


def login_logout(user: User, reader: Reader, event_time: datetime.datetime = None):
    if reader.reader_type == Reader.ReaderType.ENTRANCE:
        login(user, reader.area, event_time)
    elif reader.reader_type == Reader.ReaderType.EXIT:
        logout(user, event_time)


def login(user: User, area: Area, start: datetime.datetime = None):
    project = user.active_projects().first()
    if project:
        area_access: AreaAccessRecord = user.area_access_record()
        # If user is logged in a different area, automatically log him out
        if area_access and area_access.area != area:
            logout(user, start)
        # Only log in if not already in the area
        if not area_access or area_access.area != area:
            AreaAccessRecord.objects.create(area=area, customer=user, start=start, project=project)
    else:
        rs2_logger.error(f"no active projects found for user {user}, skipping log in to {area}")


def logout(user: User, end: datetime.datetime):
    area_access: AreaAccessRecord = user.area_access_record()
    if area_access:
        for project_id in get_project_ids_to_charge_for_user(user, area_access.start, end):
            refresh_access: AreaAccessRecord = AreaAccessRecord.objects.get(pk=area_access.id)
            refresh_access.project_id = project_id
            if not refresh_access.end:
                # update current record
                refresh_access.end = end
            else:
                # We are creating a copy for each project the user worked on
                refresh_access.pk = None
                refresh_access.id = None
            refresh_access.save()

        # Dealing with reservation and staff charges, to be consistent with NEMO
        shorten_reservation(user, area_access.area, end)
        # Stop charging area access if staff is leaving the area
        staff_charge = user.get_staff_charge()
        if staff_charge:
            try:
                staff_area_access = AreaAccessRecord.objects.get(staff_charge=staff_charge, end=None)
                staff_area_access.end = timezone.now()
                staff_area_access.save()
            except AreaAccessRecord.DoesNotExist:
                pass
    else:
        rs2_logger.warning(f"user {user} logged out but was not previously logged in to any areas")


def get_project_ids_to_charge_for_user(
    user: User, start: datetime.datetime, end: datetime.datetime
) -> Union[List, Set]:
    """
    Figure out which project to charge for the user, given a datetime
    1. If the user has only one active project, use it
    2. Be smart and check tool usage for this user (non-remote)
    3. No tool usage, use default project
    4. No default project, use first active project
    """
    if len(user.active_projects()) == 1:
        return list(user.active_projects().values_list("id", flat=True))
    ongoing_events = (
        UsageEvent.objects.filter(user=user, end__isnull=True)
        .exclude(remote_work=True)
        .exclude(start__lt=start)
        .exclude(start__gt=end)
    )
    other_events = (
        UsageEvent.objects.filter(user=user, end__isnull=False)
        .exclude(remote_work=True)
        .exclude(start__lt=start, end__lt=start)
        .exclude(start__gt=end, end__gt=end)
    )
    project_ids = list(
        distinct_qs_value_list(ongoing_events, "project_id") | distinct_qs_value_list(other_events, "project_id")
    )
    if project_ids:
        return project_ids
    else:
        try:
            default_project_id = user.get_preferences().default_project.default_project_id
            if default_project_id:
                return [default_project_id]
        except:
            pass
        return [user.active_projects().first().id]
