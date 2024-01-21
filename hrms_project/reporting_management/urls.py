from django.urls import path
from .views import department_report, department_details

urlpatterns = [
    path('department-report/', department_report, name='department_report'),
    path('department-details/<str:department_name>/', department_details, name='department_details'),
]

