# Generated by Django 4.2 on 2024-07-18 12:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getotp', '0002_alter_otprequest_valid_form_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otprequest',
            name='valid_form',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 18, 12, 14, 35, 72053, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='otprequest',
            name='valid_until',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 18, 12, 16, 35, 72053, tzinfo=datetime.timezone.utc)),
        ),
    ]
