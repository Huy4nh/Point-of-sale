# Generated by Django 4.2 on 2024-05-18 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_Catalog_Management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to='D:\\Lập trình web\\laptrinhweb_2\\Cuoi ky\\Đồ án cuối kỳ\\Point_of_Sale\\static\\image\\home\\products'),
        ),
    ]
