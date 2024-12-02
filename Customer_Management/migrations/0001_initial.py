# Generated by Django 4.2 on 2024-05-25 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='purchase_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.IntegerField()),
                ('money_give', models.IntegerField()),
                ('paid_back', models.IntegerField()),
                ('date_purchase', models.DateTimeField(auto_now=True)),
                ('product_quantity', models.IntegerField()),
            ],
        ),
    ]
