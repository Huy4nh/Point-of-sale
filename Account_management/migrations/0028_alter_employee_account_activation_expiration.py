# Generated by Django 4.2 on 2024-05-24 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account_management', '0027_alter_employee_account_activation_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_account',
            name='activation_expiration',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 24, 12, 11, 39, 620223, tzinfo=datetime.timezone.utc)),
        ),
    ]
