# Generated by Django 4.2 on 2024-05-18 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_Catalog_Management', '0009_alter_products_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.ImageField(null=True, upload_to='product/'),
        ),
    ]
