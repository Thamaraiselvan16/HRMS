from django.shortcuts import render
from emp_management.models import Employee

def home(request):
    employees=Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})