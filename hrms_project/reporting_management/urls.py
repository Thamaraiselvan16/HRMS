# reporting/urls.py

# from django.urls import path
# # from .views import department_report, present_employee_report
# from. import views
# urlpatterns = [
#     path('department_report/', views.department_report, name='department_report'),
#     path('department_details/<str:department_name>/', views.department_details, name='department_details'),
#     path('today_present_report/', views.today_present_report, name='today_present_report'),
#     path('today_present_details/<str:department_name>/', views.today_present_details, name='today_present_details'),
#     path('today_absent_report/', views.today_absent_report, name='today_absent_report'),
#     path('today_absent_details/<str:department_name>/', views.today_absent_details, name='today_absent_details'),
# ]


# reporting/urls.py

# urls.py

# urls.py

from django.urls import path
from .views import department_report, department_details

urlpatterns = [
    path('department-report/', department_report, name='department_report'),
    path('department-details/<str:department_name>/', department_details, name='department_details'),
]

