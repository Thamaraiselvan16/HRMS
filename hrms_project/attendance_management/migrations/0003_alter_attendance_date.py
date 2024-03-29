# Generated by Django 4.2.9 on 2024-01-21 11:17

import attendance_management.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("attendance_management", "0002_alter_attendance_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendance",
            name="date",
            field=models.DateField(
                unique=True,
                validators=[attendance_management.models.validate_date_not_future],
            ),
        ),
    ]
