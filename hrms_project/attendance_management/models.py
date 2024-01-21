from django.core.exceptions import ValidationError
from django.db import models
from emp_management.models import Employee
from django.utils import timezone
# Create your models here.

# Custom validator function
def validate_date_not_future(value):
    if value > timezone.now().date():
        raise ValidationError("Date should be less than or equal to the current date.")

# attendance of employees "present or absent"
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(validators=[validate_date_not_future])
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.employee.name} - {self.date} - {self.status}"
