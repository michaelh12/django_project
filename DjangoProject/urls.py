"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

from pages import views as pages_views
from products.views import product_detail_vew, product_create_view

urlpatterns = [
    path('', pages_views.home_view, name='home'),
    path('contact/', pages_views.contact_view, name='home'),
    path('social/', pages_views.social_view, name='home'),
    path('about/', pages_views.about_view, name='home'),
    path('create/', product_create_view),
    path('products/', product_detail_vew),
    path('admin/', admin.site.urls),
]
