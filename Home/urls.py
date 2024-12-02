from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('huyanh/creater/',views.index),

    path('products/', views.product_list,name='product_list'),
    path('delete-product/<str:barcode>/',views.delete_product,name='delete-product'),
    path('add_product/', views.add_new_product, name='add_product'),

    path('accounts/', views.account_list,name='account_list'),
    path('delete-account/<str:staff_id>/',views.delete_account,name='delete-account'),
    path('add_account/',views.add_new_account,name='add_account'),
    path('activate/<uuid:activation_code>/',views.activate_account,name='activate_account'),
    path('change-password/', views.change_password, name='change_password'),
    path('change-username/', views.change_username, name='change_username'),
    path('load_username_form/', views.load_username_form, name='load_username_form'),
    path('load_password_form/', views.load_password_form, name='load_password_form'),
    
    path('accounts/login/', views.login_view, name='login'),
    path('home/',views.home_view,name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home_view, name='home'),

    path('create_transaction/',views.transaction_working,name='transaction_create'),
    path('show_item/',views.show_item,name='item'),
    path('submit_transaction/',views.submit_transaction,name='submit_transaction'),
    path('check_customer_phone/',views.phone_check,name='phone_check'),
    path('purchase_wait/',views.purchase_wait,name='purchasing_wait')
]  
