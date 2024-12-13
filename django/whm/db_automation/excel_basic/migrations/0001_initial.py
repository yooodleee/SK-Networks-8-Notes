# Generated by Django 5.1.4 on 2024-12-11 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ExcelBasicEmployee",
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
                ("name", models.CharField(max_length=32)),
                ("age", models.IntegerField()),
                ("city", models.CharField(max_length=64)),
                ("score", models.IntegerField()),
                ("department", models.CharField(max_length=32)),
            ],
            options={
                "db_table": "excel_basic_employee",
            },
        ),
    ]