from django.urls import path
from .api import EmployeeCreateAPI


urlpatterns = [
    path('api/create', EmployeeCreateAPI.as_view()),
]
