from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee_account

@receiver(post_save, sender=Employee_account)
def update_employee_account(sender, instance, **kwargs):
    instance.save()