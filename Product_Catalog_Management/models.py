from django.db import models

# Create your models here.
class products(models.Model):
    barcode=models.CharField(max_length=30,primary_key=True) 
    product_name=models.CharField(max_length=50) 
    import_price=models.IntegerField()
    retail_price=models.IntegerField()
    category=models.CharField(max_length=20)
    creation_date=models.DateField()
    product_image = models.ImageField(upload_to='product/',null=True)
    def __str__(self):
        return self.product_name