# Generated by Django 4.2 on 2024-05-26 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product_Catalog_Management', '0010_alter_products_product_image'),
        ('Transaction_Processing', '0004_transaction_processing_create_date'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='transaction_processing',
            unique_together={('barcode_t', 'customer_phone', 'is_purchased')},
        ),
    ]
