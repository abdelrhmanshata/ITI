from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from . import views
from .views import *

urlpatterns = [
    # Class View
    # path("update/<int:productID>", UpdateProduct.as_view(), name="product-update"),
    # Class Base Generic
    path("", ListProductGeneric.as_view(), name="Products"),
    path(
        "addNewProduct",
        login_required(CreateProductGeneric.as_view()),
        name="addNewProduct",
    ),
    path("details/<pk>", DetailProductGeneric.as_view(), name="product-details"),
    path(
        "update/<pk>",
        login_required(UpdateProductGeneric.as_view()),
        name="product-update",
    ),
    path(
        "delete/<pk>",
        login_required(DeleteProductGeneric.as_view()),
        name="deleteProduct",
    ),
    path("category", views.category, name="category"),
    path("aboutUS", views.aboutUS, name="aboutUS"),
    # Class View
    path(
        "addNewCategory", login_required(AddCategory.as_view()), name="addNewCategory"
    ),
]
