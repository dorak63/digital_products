# Generated by Django 4.2 on 2024-07-13 10:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_modified_province_modified_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.BigIntegerField(blank=True, error_messages={'unique': 'A user with this mobile number already exists.'}, null=True, unique=True, validators=[django.core.validators.RegexValidator('^989[0-3,9]\\d{8}$', 'Enter a valid mobile number.', 'invalid')], verbose_name='mobile number'),
        ),
    ]