# Generated by Django 4.2.9 on 2024-01-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("emp_management", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
