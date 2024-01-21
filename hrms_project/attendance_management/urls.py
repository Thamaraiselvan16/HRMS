from django.urls import path
from. import views

urlpatterns = [
    path('mark_attendance/<int:employee_id>/', views.mark_attendance, name='mark_attendance'),
    path('attendance_details/<int:employee_id>/', views.attendance_details, name='attendance_details'),
]