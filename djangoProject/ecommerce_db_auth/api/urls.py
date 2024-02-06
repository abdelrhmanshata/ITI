from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *


urlpatterns = [
    # path("hello/", hello, name="hello"),
    # Category CRUD Operation
    path("allCategory/", allCategory, name="allCategory"),
    path("getCategory/<int:id>", getCategory, name="getCategory"),
    path("addCategory/", addCategory, name="addCategory"),
    path("updateCategory/<int:id>", updateCategory, name="updateCategory"),
    path("deleteCategory/<int:id>", deleteCategory, name="deleteCategory"),
]
