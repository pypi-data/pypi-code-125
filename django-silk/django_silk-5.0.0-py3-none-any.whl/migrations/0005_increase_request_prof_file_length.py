# Generated by Django 1.11.3 on 2017-07-31 23:40

from django.db import migrations, models

import silk.models


class Migration(migrations.Migration):

    dependencies = [
        ('silk', '0004_request_prof_file_storage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='prof_file',
            field=models.FileField(max_length=300, null=True, storage=silk.models.silk_storage, upload_to=''),
        ),
    ]
