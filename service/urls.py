from django.urls import path

from .api import HelloAPI

urlpatterns = [
    path('hello', HelloAPI.as_view()),
]
