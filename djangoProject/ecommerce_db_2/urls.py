from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.products, name="Products"),
    path("update/<int:productID>", views.productUpdate, name="product-update"),
    path("details/<int:productID>", views.productDetails, name="product-details"),
    path("delete/<int:productID>", views.deleteProduct, name="deleteProduct"),
    path("category", views.category, name="category"),
    path("aboutUS", views.aboutUS, name="aboutUS"),
    path("addNewProduct", views.addNewProduct, name="addNewProduct"),
    path("addNewCategory", views.addNewCategory, name="addNewCategory"),
]
