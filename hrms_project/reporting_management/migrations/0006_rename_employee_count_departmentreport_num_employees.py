# Generated by Django 4.2.9 on 2024-01-21 02:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("reporting_management", "0005_departmentreport_delete_employeereport"),
    ]

    operations = [
        migrations.RenameField(
            model_name="departmentreport",
            old_name="employee_count",
            new_name="num_employees",
        ),
    ]
