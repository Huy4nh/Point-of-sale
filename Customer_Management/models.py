from django.db import models
from Product_Catalog_Management.models import products
# Create your models here.

class customer_info(models.Model):
    name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=40)
    class Meta:
        unique_together = ('phone_number','name',)
    def __str__(self):
        return self.name

class purchase_history(models.Model):
    total_amount = models.IntegerField()
    money_give = models.IntegerField()
    paid_back = models.IntegerField()
    date_purchase = models.DateTimeField(auto_now=True)
    product_quantity= models.IntegerField()
    # fk_ph_ci=models.ForeignKey(customer_info,on_delete=models.CASCADE, related_name='customer')
    

