from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('service/', include('service.urls')),
    path('employee/', include('employee.urls')),
]
