from django.urls import path
from .api import SimpleAPI

urlpatterns = [
    path('api/hello', SimpleAPI.as_view())
]
