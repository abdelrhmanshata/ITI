from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('prefix url',view,name=sdd)
    path("", views.hello),
    path("list", views.track_list),
    path("<int:trackID>", views.track_details,name="track_details"),
    # re_path(r"^tracks/([0-9]*.[0-9]*)$", views.track_details),
]
