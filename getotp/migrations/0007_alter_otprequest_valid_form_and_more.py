# Generated by Django 4.2 on 2024-07-19 17:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getotp', '0006_alter_otprequest_valid_form_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otprequest',
            name='valid_form',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 19, 17, 49, 45, 500467, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='otprequest',
            name='valid_until',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 19, 17, 51, 45, 500467, tzinfo=datetime.timezone.utc)),
        ),
    ]
