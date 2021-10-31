from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode, urlencode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from accounts.models import Account
from .forms import RegisterForm
from customers.forms import CustomerForm
from customers.models import Customer


def home(request):
    return render(request, 'home.html')


def account_login(request):

    if request.user.is_authenticated:  # if already logged in
        return redirect(reverse('home'))
    else:

        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')

            account = authenticate(email=email, password=password)
            if account is not None:
                login(request, account)
                messages.success(request, 'You have been logged in succesfully!')
                return redirect(reverse('home'))
            else:
                messages.error(request, 'User or password is invlaid!')
    return render(request, 'account/account_login.html')


def account_logout(request):
    if not request.user.is_authenticated:  # if already logged in
        return redirect(reverse('login'))
    else:
        logout(request)
        messages.success(request, 'You have been logged out successfully!')
        return redirect(reverse('login'))



def register(request):
    if request.user.is_authenticated: # if already logged in
        return redirect(reverse('home'))
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)

            if form.is_valid():
                user = Account.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    email=form.cleaned_data.get('email'),
                    password=form.cleaned_data.get('password'),
                )
                user.save()

                email = user.email

                current_site = get_current_site(request)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)
                mail_subject = 'Account Verification'
                domain = f'http://{current_site}{reverse("account_verification", kwargs={"uidb64":uid, "token":token})}'
                context = {
                    'site_domain': domain,
                    'username': user.username,
                }
               
                message = render_to_string('account/account_verification_email.html', context)
                email_message = EmailMessage(mail_subject, message, to=[email,])
                email_message.send()
                return redirect(reverse('login') + f'?account=verification&email={email}')
            else:
                print(form.errors)
        else:
            form = RegisterForm()
        context = {
            'form': form
        }

    return render(request, 'account/register.html', context)

def account_verification(request, uidb64, token):
    try:
        id = urlsafe_base64_decode(uidb64).decode()
        user = Account.objects.get(id=id)
    except (Account.DoesNotExist, ValueError, TypeError):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        request.session['user_id'] = id
        return redirect('register_complete')
    else:
        messages.error(request, 'verification link has expired')
        return redirect('register')

def register_complete(request):
    form = CustomerForm(None)
    user_id = request.session.get('user_id')
    try:
        user = Account.objects.get(id=user_id)
    except Account.DoesNotExist:
        messages.error(request, 'Invalid link visited')
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
            messages.success(request, 'Account registration completed successfully!')
            return redirect(reverse('login'))
        else:
            form = CustomerForm(None)
        
    context = {
        'form': form,
        'reg_user': user
    }
    return render(request, 'account/register_complete.html', context)


def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = Account.objects.get(email=email)
        except Account.DoesNotExist:
            user = None

        if user is not None:
            current_site = get_current_site(request)
            mail_subject = 'Account password reset'
            context = {
                'uid': urlsafe_base64_encode(force_bytes(user.id)),
                'token': default_token_generator.make_token(user),
                'domain': current_site,
                'username': user.username
            }
            message = render_to_string('account/password_reset_email.html', context)
            email_message = EmailMessage(mail_subject, message, to=[email,])
            email_message.send()
            return redirect('password_reset_done')
        else:
            messages.error(request, 'Account with this email does not exist!')
            return redirect('password_reset')
    return render(request, 'account/password_reset.html')


def password_reset_done(request):
    return render(request, 'account/password_reset_done.html')


def password_reset_confirm(request, uidb64, token):

    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account.objects.get(id=uid)
    except(Account.DoesNotExist, TypeError, ValueError):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        request.session['id'] = uid
        return redirect('password_reset_complete')
    else:
        messages.error(request, 'Invalid link')
        return redirect('login')


def password_reset_complete(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            id = request.session.get('id')
            user = Account.objects.get(pk=id)
            user.set_password(password)
            user.save()
            messages.success(request, 'You new password has been set. You can log in below.')
            return redirect('login')
        else:
            messages.error(request, 'The two password did not match!')
            return redirect('password_reset_complete')

    return render(request, 'account/password_reset_complete.html')



def password_change(request):
    if request.method == 'POST':
        user = Account.objects.get(id=request.user.id)
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        new_password2 = request.POST.get('new_password2')

        # check if the current password entered is correct
        if user.check_password(current_password):
            if new_password == new_password2:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Your password was changed successfully!')
                logout(request)
                return redirect('login')
            else:
                messages.error(request, 'The two new password did not match!')
        else:
            messages.error(request, 'The current password is incorrect!')

    return render(request, 'account/password_change.html')
