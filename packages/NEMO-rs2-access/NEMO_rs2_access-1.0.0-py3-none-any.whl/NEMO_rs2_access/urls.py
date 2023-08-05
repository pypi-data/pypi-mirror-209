from django.urls import path

from NEMO_rs2_access import views

urlpatterns = [
    path("user_preferences/", views.custom_user_preferences, name="user_preferences")
]
