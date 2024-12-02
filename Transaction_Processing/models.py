from django.db import models
from Product_Catalog_Management.models import products
from Customer_Management.models import purchase_history,customer_info
import random as rd
import string as str_d
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
class Transaction_Processing(models.Model):
    product_name = models.CharField(max_length=30,default=None)
    quantity = models.IntegerField()
    unit_price = models.IntegerField(default=None)
    total_price = models.IntegerField(default=None)
    is_purchased = models.BooleanField(default=False)
    barcode_t= models.ForeignKey(products,on_delete=models.CASCADE,related_name='barcode_t')
    create_date = models.DateTimeField(auto_now_add=True)
    customer_phone = models.CharField(max_length=15,default='waiting')

    def setid(self,a):
        return ''.join(rd.choices(str_d.ascii_uppercase + str_d.digits, k=a))
    def save(self,*args, **kwargs):
        if self.unit_price is None:
            try:
                product=products.objects.get(barcode=self.barcode_t.barcode)
                self.unit_price=product.retail_price
            except ObjectDoesNotExist:
                print("Không tìm thấy sản phẩm")
        if self.total_price is None:
            product=products.objects.get(barcode=self.barcode_t.barcode)
            self.total_price=int(self.quantity)*int(product.retail_price)
        super().save(*args, **kwargs)


