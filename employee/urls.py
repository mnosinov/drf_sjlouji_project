from django.urls import path
from .api import EmployeeCreateAPI, EmployeeAPI, EmployeeUpdateAPI, EmployeeDeleteAPI


urlpatterns = [
    path('api', EmployeeAPI.as_view()),
    path('api/create', EmployeeCreateAPI.as_view()),
    path('api/<int:pk>', EmployeeUpdateAPI.as_view()),
    path('api/<int:pk>/delete', EmployeeDeleteAPI.as_view()),
]
