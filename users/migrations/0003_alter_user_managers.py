# Generated by Django 4.2 on 2024-07-11 16:53

from django.db import migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
    ]
