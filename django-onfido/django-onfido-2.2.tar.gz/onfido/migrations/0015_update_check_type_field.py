# Generated by Django 3.1.6 on 2021-02-08 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("onfido", "0014_update_status_result_choices"),
    ]

    operations = [
        migrations.AlterField(
            model_name="check",
            name="check_type",
            field=models.CharField(
                blank=True,
                help_text="DEPRECATED: Check objects no longer support a type.",
                max_length=10,
                null=True,
            ),
        ),
        migrations.RenameField(
            model_name="check",
            old_name="check_type",
            new_name="x_check_type",
        ),
    ]
