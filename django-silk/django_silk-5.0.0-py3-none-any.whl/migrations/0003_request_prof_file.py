# Generated by Django 1.9.7 on 2016-07-08 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silk', '0002_auto_update_uuid4_id_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='prof_file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
