# Generated by Django 4.2.9 on 2024-01-21 02:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "reporting_management",
            "0004_employeereport_delete_attendancereport_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="DepartmentReport",
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
                ("employee_count", models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name="EmployeeReport",
        ),
    ]