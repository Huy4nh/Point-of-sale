# Generated by Django 4.2 on 2024-05-17 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('barcode', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('import_price', models.IntegerField()),
                ('retail_price', models.IntegerField()),
                ('category', models.CharField(max_length=20)),
                ('creation_date', models.DateField()),
            ],
        ),
    ]
