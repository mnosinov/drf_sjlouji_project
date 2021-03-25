from rest_framework import generics

from .serializer import EmployeeSerializer
from .models import Employee


class EmployeeAPI(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    # queryset = Employee.objects.all()

    def get_queryset(self):
        return Employee.objects.all()


class EmployeeCreateAPI(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeUpdateAPI(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDeleteAPI(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
