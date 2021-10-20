from django.contrib import auth
from django.http.request import RAISE_ERROR
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode, urlencode
from django.utils.encoding import force_bytes

from accounts.models import Account
from .forms import RegisterForm
from customers.forms import CustomerForm
from customers.models import Customer


def home(request):
    return render(request, 'home.html')


def account_login(request):

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        account = authenticate(email=email, password=password)
        if account is not None:
            login(request, account)
            messages.success(request, 'You have been logged in succesfully!')
            return redirect('/')
        else:
            messages.error(request, 'User or password is invlaid!')
    return render(request, 'account/account_login.html')


def account_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('/account/account_login/')



def register(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = Account.objects.create_user(
                username=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password'),
            )
            user.save()
        
            return redirect(f'/account/register_complete/?user={user.id}')
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    context = {
        'form': form
    }

    return render(request, 'account/register.html', context)

def register_complete(request):
    
    try:
        id = request.GET.get('user')
        user = Account.objects.get(id=id)
    except Account.DoesNotExist:
        print('No user')

    if request.method == 'POST': 
        form = CustomerForm(request.POST)      
        if form.is_valid():
            customerAccount = Account.objects.get(email=request.POST['email'])

            # add customer information to database
            customer = Customer.objects.create(
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                middle_name=form.cleaned_data.get('middle_name'),
                gender=form.cleaned_data.get('gender'),
                phone=form.cleaned_data.get('phone'),
                address_1=form.cleaned_data.get('address_1'),
                address_2=form.cleaned_data.get('address_2'),
                city=form.cleaned_data.get('city'),
                state=form.cleaned_data.get('state'),
                country=form.cleaned_data.get('country'),
                account=customerAccount,
                email=customerAccount.email
            )

            # make account active for login
            customerAccount.is_active = True
            customerAccount.save()

            customer.save()
            return redirect('/')
    else:
        form = CustomerForm()
        
    context = {
        'form': form,
        'reg_user': user
    }
    return render(request, 'account/register_complete.html', context)
