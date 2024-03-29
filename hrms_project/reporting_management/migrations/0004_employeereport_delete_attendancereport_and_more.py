# Generated by Django 4.2.9 on 2024-01-21 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("emp_management", "0001_initial"),
        (
            "reporting_management",
            "0003_attendancereport_departmentreport_employeedetails_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="EmployeeReport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("department", models.CharField(max_length=50)),
                ("date", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[("Present", "Present"), ("Absent", "Absent")],
                        max_length=10,
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="emp_management.employee",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="AttendanceReport",
        ),
        migrations.DeleteModel(
            name="DepartmentReport",
        ),
        migrations.DeleteModel(
            name="EmployeeDetails",
        ),
    ]
