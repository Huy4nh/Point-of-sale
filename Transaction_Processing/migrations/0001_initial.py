# Generated by Django 4.2 on 2024-05-25 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Product_Catalog_Management', '0010_alter_products_product_image'),
        ('Customer_Management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction_Processing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default=None, max_length=30)),
                ('quantity', models.IntegerField()),
                ('unit_price', models.IntegerField(default=None)),
                ('total_price', models.IntegerField(default=None)),
                ('is_purchased', models.BooleanField(default=False)),
                ('barcode_t', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barcode_t', to='Product_Catalog_Management.products')),
                ('customer_t', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='Customer_Management.customer_info')),
            ],
            options={
                'unique_together': {('barcode_t', 'customer_t')},
            },
        ),
    ]