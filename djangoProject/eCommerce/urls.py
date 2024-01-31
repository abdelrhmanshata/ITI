from django.urls import path, re_path
from . import views

urlpatterns = [   
    path("", views.products,name="Products"),
    path("<int:productID>", views.productDetails,name="product-details"),
    path("category", views.category,name="category"),
    path("aboutUS", views.aboutUS,name="aboutUS"),
]
