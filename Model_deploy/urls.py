# FER_deploy/Model_deploy/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # This maps the root URL of our app to the predict_emotion view
    path('', views.predict_emotion, name='predict_emotion'),
]