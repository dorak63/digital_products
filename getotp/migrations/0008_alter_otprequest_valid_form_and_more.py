# Generated by Django 4.2 on 2024-07-19 19:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getotp', '0007_alter_otprequest_valid_form_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otprequest',
            name='valid_form',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 19, 19, 1, 39, 679202, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='otprequest',
            name='valid_until',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 19, 19, 3, 39, 679202, tzinfo=datetime.timezone.utc)),
        ),
    ]
