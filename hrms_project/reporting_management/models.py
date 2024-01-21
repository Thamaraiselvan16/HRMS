from django.db import models
from emp_management.models import Employee

# no. of employee in department used to chart
class EmployeeReport(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department = models.CharField(max_length=50)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.employee.name} - {self.date} - {self.status}"
