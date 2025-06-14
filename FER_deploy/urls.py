"""
URL configuration for FER_deploy project.

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
# FER_deploy/FER_deploy/urls.py

from django.contrib import admin
from django.urls import path, include # Make sure to import 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    # This tells Django to use the URLs from your Model_deploy app
    # for any request that isn't for '/admin/'
    path('', include('Model_deploy.urls')), 
]