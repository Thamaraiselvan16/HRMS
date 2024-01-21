from django.shortcuts import render
from emp_management.models import Employee
from django.db.models import Count
# from datetime import date
# from .models import EmployeeReport


# department report for number employees in the department
def department_report(request):
    department_counts = Employee.objects.values('department').annotate(count=Count('id'))
    return render(request, 'reporting_management/department_report.html', {'department_counts': department_counts})

# department details report for number employees in the department (it will show the details about selected department)
def department_details(request, department_name):
    department_employees = Employee.objects.filter(department=department_name)
    return render(request, 'reporting_management/department_details.html', {'department_employees': department_employees})

