# Generated by Django 4.2 on 2024-05-24 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account_management', '0021_alter_employee_account_activation_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_account',
            name='activation_expiration',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 24, 11, 57, 25, 158287, tzinfo=datetime.timezone.utc)),
        ),
    ]
