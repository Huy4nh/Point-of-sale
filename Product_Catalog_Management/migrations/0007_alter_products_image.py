# Generated by Django 4.2 on 2024-05-18 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_Catalog_Management', '0006_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
