from django.urls import path
from .api import SimpleAPI, RegisterAPI

urlpatterns = [
    path('api/hello', SimpleAPI.as_view()),
    path('api/register', RegisterAPI.as_view()),
]
