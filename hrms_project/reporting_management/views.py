from django.shortcuts import render
from emp_management.models import Employee
from .models import EmployeeReport
from django.db.models import Count
from datetime import date

def department_report(request):
    department_counts = Employee.objects.values('department').annotate(count=Count('id'))
    return render(request, 'reporting_management/department_report.html', {'department_counts': department_counts})

def department_details(request, department_name):
    department_employees = Employee.objects.filter(department=department_name)
    return render(request, 'reporting_management/department_details.html', {'department_employees': department_employees})

