from django.urls import path, re_path
from . import views
from .views import *
from django.contrib.auth.views import *
from django.urls import path, re_path, include

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("profile/", views.myProfile, name="myProfile"),
    path("register/", myRegistration.as_view(), name="myRegistration"),
]
