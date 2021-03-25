from rest_framework import generics

from .serializer import EmployeeSerializer
from .models import Employee


class EmployeeCreateAPI(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
