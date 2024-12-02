from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse,HttpResponseBadRequest
from Product_Catalog_Management.models import products
from Account_management.models import  Employee_account
from .forms import ProductForm,AccountForm,LoginForm,UsernameChangeForm,CustomPasswordChangeForm,TransactionForm,customerForm
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import os
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from Transaction_Processing.models import Transaction_Processing
from Customer_Management.models import customer_info
# Create your views here.
@csrf_exempt
def index(request):
    check=Employee_account.objects.all()
    test=True
    for i in check:
        if test==True:
            i.delete()
        if i.activation_expiration < timezone.now() and i.is_active == False:
            i.delete()
    return render(request,'pages/home.html',{'user': 'creater'})
# --------------------------------------------LOGIN---------------------------------------------------------------------------------------
@csrf_exempt
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user=Employee_account.objects.get(username=username)
            except:
                messages.error(request, 'Không tìm thấy tài khoản.')
        
            check = (password == user.password)
            print(user)
            if check:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'Tài khoản chưa được kích hoạt.')
            else:
                messages.error(request, 'Sai thông tin đăng nhập.')
    else:
        form = LoginForm()
    return render(request, 'pages/login.html', {'form': form})

@login_required
def home_view(request):
    can_register = request.user.is_admin
    can_view_accounts = request.user.is_admin
    return render(request, 'pages/home.html', {'can_register': can_register, 'can_view_accounts': can_view_accounts})
@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect('login')


# --------------------------------------------PRODUCT MANAGEMENT-----------------------------------------------------------------------------
def product_list(request):
    products_list=products.objects.all()
    data = [{'barcode':product.barcode,'product_name': product.product_name, 'import_price': product.import_price, 'retail_price': product.retail_price, 'product_image':settings.MEDIA_URL+str(product.product_image)} for product in products_list]
    return JsonResponse(data,safe=False)

@csrf_exempt
def delete_product(request,barcode):
    if request.method=='POST':
        try:
            product = products.objects.get(barcode=barcode)
            products.delete(product)
            os.remove('media/'+str(product.product_image))
            return JsonResponse({'status':'success'},safe=False)
        except products.DoesNotExist:
            return JsonResponse({'status':'error','message':'Product does not exist'},safe=False)
    return JsonResponse({'status':'error','messsage':'Invalid request'},safe=False)

@csrf_exempt
def add_new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ProductForm()
        return render(request, 'pages/add_product_form.html', {'form': form})
    
# --------------------------------------------ACCOUNT MANAGEMENT-----------------------------------------------------------------------------
def account_list(request):
    accounts_lists=Employee_account.objects.all()
    data = [{'staff_id':account.staff_id,'username': account.username, 'gmail': account.gmail, 'is_admin': account.is_admin, 'avatar':settings.MEDIA_URL+str(account.avatar)} for account in accounts_lists]
    return JsonResponse(data,safe=False)
@csrf_exempt
def delete_account(request,staff_id):
    if request.method=='POST':
        try:
            account = Employee_account.objects.get(staff_id=staff_id)
            os.remove('media/'+str(account.avatar))
            products.delete(account)
            return JsonResponse({'status':'success'},safe=False)
        except products.DoesNotExist:
            return JsonResponse({'status':'error','message':'Account does not exist'},safe=False)
    return JsonResponse({'status':'error','messsage':'Invalid request'},safe=False)

@csrf_exempt
def add_new_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST,request.FILES)
        if form.is_valid():
            staff_account = form.save(commit=False)
            print(staff_account.activation_code)
            staff_account.save()
            activation_link = f"{request.build_absolute_uri('/activate/')}{staff_account.activation_code}/"
            send_mail('Kich hoat tai khoan',f'nhan vao duong dan nay de kich hoat:{activation_link}',settings.DEFAULT_FROM_EMAIL,[staff_account.gmail])
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = AccountForm()
        print(form)
        return render(request, 'pages/add_account_form.html',{'form':form})
    
@csrf_exempt
def activate_account(request,activation_code):
    try:
        staff_account=Employee_account.objects.get(activation_code=activation_code)
        print(staff_account.activation_expiration)
        print(staff_account.activation_expiration > timezone.now())
        if staff_account.activation_expiration > timezone.now():
            staff_account.is_active=True
            staff_account.save()
            return render(request,'pages/activation_success.html')
        else:
            staff_account.delete()
            return render(request,'pages/activation_failure.html')
    except:
        redirect('activation_failure')
        return render(request,'pages/activation_failure.html')
    

@login_required
def change_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        # Tạo mật khẩu mới nhưng không mã hóa
        request.user.password = new_password
        request.user.save(update_fields=['password'])  # Cập nhật chỉ trường password
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

@login_required
def change_username(request):
    if request.method == 'POST':
        new_username = request.POST.get('new_username')
        request.user.username = new_username
        request.user.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

@login_required
def load_username_form(request):
    print('day ne')
    form = UsernameChangeForm(instance=request.user)
    return render(request, 'pages/change_username.html', {'form': form})

@login_required
def load_password_form(request):
    print('day ne')
    form = CustomPasswordChangeForm(instance=request.user)
    return render(request, 'pages/change_password.html', {'form': form})



# --------------------------------------------ACCOUNT MANAGEMENT-----------------------------------------------------------------------------
@csrf_exempt
def transaction_working(request):
    clearing_transaction()
    if request.method == 'POST':
        tmp_barcode=request.POST.get('barcode')
        quantity=request.POST.get('quantity')
        try:
            tmp_product=products.objects.get(barcode=tmp_barcode)
            product_name=tmp_product.product_name
        except:    
            return HttpResponseBadRequest('Missing barcode or quantity')
        check_barcode=Transaction_Processing.objects.filter(barcode_t=tmp_barcode)
        if check_barcode.exists():
            check_cus_exist=Transaction_Processing.objects.filter(customer_phone='waiting')
            check_purchased=check_cus_exist.filter(is_purchased=False)
            if check_cus_exist.exists() and check_purchased.exists():
                inc_quan_tran=Transaction_Processing.objects.get(customer_phone='waiting',barcode_t=tmp_barcode,is_purchased=False)
                quantity=int(inc_quan_tran.quantity)+int(quantity)
                total_price=int(quantity)*int(tmp_product.retail_price)
                inc_quan_tran.total_price=total_price
                inc_quan_tran.quantity=quantity
                inc_quan_tran.id=inc_quan_tran.id
                inc_quan_tran.save()
                return JsonResponse({'success': True})
        transaction=Transaction_Processing.objects.create(product_name=product_name,barcode_t=tmp_product,quantity=quantity)
        return JsonResponse({'success': True})
    else:
        form = TransactionForm()
        return render(request,'pages/transaction_work.html',{'form':form})

def clearing_transaction():
    chk=Transaction_Processing.objects.all()
    for i in chk:
        print(timezone.now())
        print(i.create_date +timezone.timedelta(minutes=10))
        if i.is_purchased == False and (i.create_date +timezone.timedelta(minutes=10)) < timezone.now():
            print(i.create_date +timezone.timedelta(minutes=10))
            i.delete()


@csrf_exempt
def show_item(request):
    total=0
    items=Transaction_Processing.objects.filter(is_purchased=False)
    for i in items:
        total=total+int(i.total_price)
        i.img=settings.MEDIA_URL+str(i.barcode_t.product_image)
    return render(request,'pages/item.html',{'items':items,'total':total})

@csrf_exempt
def submit_transaction(request):
    if request.method=="POST":
        form = customerForm(request.POST)
        if form.is_valid():
            try:
                customer=form.save(commit=False)
                customer.save()
                now_tran=Transaction_Processing.objects.filter(customer_phone='waiting')
                for tran in now_tran:
                    tran.customer_phone=customer.phone_number
                    tran.save()
                return JsonResponse({'success': True})
            except:
                now_tran=Transaction_Processing.objects.filter(customer_phone='waiting')
                for tran in now_tran:
                    tran.customer_phone=customer
                    tran.save()
                return JsonResponse({'success': True})
        else:
            phone_number=request.POST['phone_number']
            now_tran=Transaction_Processing.objects.filter(customer_phone='waiting')
            for tran in now_tran:
                tran.customer_phone=phone_number
                tran.save()
            return JsonResponse({'success': True})
    else:
        form = customerForm()
        return render(request,'pages/customer_form.html',{'form':form})

@csrf_exempt
def purchase_wait(request):
    if request.method == 'POST':
        phone_number=request.POST['phone_number']
        tmp=Transaction_Processing.objects.filter(customer_phone=phone_number)
        for i in tmp:
            i.is_purchased=True
            i.save()
        return JsonResponse({'success':True})
    else:
        try:
            a=[]
            wait_pur=Transaction_Processing.objects.filter(is_purchased=False)
            tmp=''
            reponse=[]
            for i in wait_pur:
                if tmp!=i.customer_phone:
                    tmp=i.customer_phone
                    a.append(tmp)
            for phone in a:
                tmp=Transaction_Processing.objects.filter(is_purchased=False,customer_phone=phone)
                total=0
                name=customer_info.objects.filter(phone_number=phone).first().name
                item_quantity=tmp.__len__()
                phone_number=phone
                create_date=tmp.first().create_date
                for i in tmp:
                    total=total+i.total_price
                reponse.append({'name':name,'item_quantity':item_quantity,'create_date':create_date,'phone_number':phone_number,'total_price':total})  
                                      
        except:
            reponse={}
       
        return render(request,'pages/checking_purchase.html',{'reponse':reponse,})

@csrf_exempt
def phone_check(request):
    phone_number=request.GET.get('phone')
    try:
        customer= customer_info.objects.get(phone_number=phone_number)
        reponse={'name':customer.name,'address':customer.address}
    except:
        reponse={'name':'','address':''}
    return JsonResponse(reponse)
    

