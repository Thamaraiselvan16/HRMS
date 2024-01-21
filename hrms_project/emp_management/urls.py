from django.urls import path
from. import views

urlpatterns = [
    
    # path('',views.home, name='home'),
    path('employee_list/',views.employee_list, name='employee_list'),
    path('add_employee/',views.add_employee, name='add_employee'),
    path('employee_list_pdf/', views.employee_list_pdf, name='employee_list_pdf'),
    path('employee_list_csv/', views.employee_list_csv, name='employee_list_csv'),
    path('update_employee/<int:employee_id>/', views.update_employee, name='update_employee'),  
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),  
]