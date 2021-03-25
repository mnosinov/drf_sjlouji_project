from django.urls import path

from .api import Hello1API, Hello2API

urlpatterns = [
    path('hello1', Hello1API.as_view()),
    path('hello2/<str:name>', Hello2API.as_view()),
]
