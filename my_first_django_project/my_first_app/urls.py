"""
URL configuration for my_first_django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from .views import hello_world, redirect_example, json_example, show_cookies

urlpatterns = [
    path('hello/<str:name>/', hello_world, name='hello_world_with_name'),
    path('redirect/', redirect_example, name='redirect_example'),
    path('json/', json_example, name='json_example'),
    path('cookies/', show_cookies, name='show_cookies'),
]
