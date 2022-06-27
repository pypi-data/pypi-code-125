# Generated by Django 3.2.13 on 2022-05-24 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("onfido", "0018_remove_isclear_from_basestatus_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="check",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("awaiting_applicant", "Awaiting applicant"),
                    ("awaiting_approval", "Awaiting approval"),
                    ("awaiting_data", "Awaiting data"),
                    ("cancelled", "Cancelled"),
                    ("complete", "Complete"),
                    ("expired", "Expired"),
                    ("in_progress", "In progress"),
                    ("paused", "Paused"),
                    ("reopened", "Reopened"),
                    ("withdrawn", "Withdrawn"),
                ],
                db_index=True,
                help_text="The current state of the check / report (from API).",
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="report",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("awaiting_applicant", "Awaiting applicant"),
                    ("awaiting_approval", "Awaiting approval"),
                    ("awaiting_data", "Awaiting data"),
                    ("cancelled", "Cancelled"),
                    ("complete", "Complete"),
                    ("expired", "Expired"),
                    ("in_progress", "In progress"),
                    ("paused", "Paused"),
                    ("reopened", "Reopened"),
                    ("withdrawn", "Withdrawn"),
                ],
                db_index=True,
                help_text="The current state of the check / report (from API).",
                max_length=20,
                null=True,
            ),
        ),
    ]
