from django import forms
from Product_Catalog_Management.models import products
from Account_management.models import Employee_account
from django.contrib.auth import authenticate
from Transaction_Processing.models import Transaction_Processing
from Customer_Management.models import customer_info

class ProductForm(forms.ModelForm):
    class Meta:
        model = products
        fields = ['barcode','product_name','import_price','retail_price','category','creation_date','product_image']
    
class AccountForm(forms.ModelForm):
    class Meta:
        model = Employee_account
        fields = ['staff_id','gmail','is_admin','avatar']
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model = Employee_account
        fields = ['username']

class CustomPasswordChangeForm(forms.ModelForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Employee_account
        fields = []

    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password")
        if not self.instance.check_password(old_password):
            raise forms.ValidationError("Your old password was entered incorrectly. Please enter it again.")
        return old_password

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError("The two new password fields must match.")
        return cleaned_data

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data["new_password1"])
        if commit:
            user.save()
        return user

class TransactionForm(forms.ModelForm):
    barcode=forms.CharField(widget=forms.TextInput())
    quantity= forms.IntegerField(widget=forms.TextInput())
    class Meta:
        model=Transaction_Processing
        fields=[]

    
    def clean(self):
        cleaned_data=super().clean()
        barcode=cleaned_data.get("barcode")
        quantity=cleaned_data.get("quantity")
        try:
            product=products.objects.get(barcode=barcode)
            return product
        except:
            raise forms.ValidationError("There no product match with barcode")

class customerForm(forms.ModelForm):
    class Meta:
        model = customer_info
        fields=['phone_number','name','address']