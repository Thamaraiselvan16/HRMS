from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Employee(models.Model):
    name = models.CharField(max_length=100, unique=True)
    designation = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    date_of_joining = models.DateField()

    def __str__(self):
        return self.name

    def clean(self):
        # Ensure date_of_joining is less than or equal to the current date
        if self.date_of_joining and self.date_of_joining > timezone.now().date():
            raise ValidationError("Date of joining must be less than or equal to the current date.")

    class Meta:
        # Add a constraint to the model to enforce the condition at the database level
        constraints = [
            models.CheckConstraint(
                check=models.Q(date_of_joining__lte=timezone.now().date()),
                name='date_of_joining_must_be_less_than_or_equal_to_current_date'
            ),
        ]

