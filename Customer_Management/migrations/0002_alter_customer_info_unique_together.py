# Generated by Django 4.2 on 2024-05-25 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer_Management', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='customer_info',
            unique_together={('phone_number', 'name')},
        ),
    ]