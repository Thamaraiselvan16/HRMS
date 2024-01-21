# Generated by Django 4.2.9 on 2024-01-21 11:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "emp_management",
            "0003_employee_date_of_joining_must_be_less_than_current_date",
        ),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="employee",
            name="date_of_joining_must_be_less_than_current_date",
        ),
        migrations.AddConstraint(
            model_name="employee",
            constraint=models.CheckConstraint(
                check=models.Q(("date_of_joining__lte", datetime.date(2024, 1, 21))),
                name="date_of_joining_must_be_less_than_or_equal_to_current_date",
            ),
        ),
    ]