"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path, include
from accounts import views
from .settings import *
from django.conf.urls.static import static

urlpatterns = [
    # path('prefix url',view,name=sdd)
    path("admin/", admin.site.urls),
    # path("", include("eCommerce.urls")),
    # path("", include("ecommerce_db.urls")),
    # path("", include("ecommerce_db_2.urls")),
    path("", include("ecommerce_db_auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("Category/API/", include("ecommerce_db_auth.api.urls")),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
