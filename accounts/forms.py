from django import forms
from django.core.exceptions import ValidationError

from .models import Account


class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'password2']
        widgets = {
            'password': forms.PasswordInput(attrs={'type': 'password', 'placeholder': 'Password'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email address'}),
        }

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']

        existin_user = Account.objects.filter(username=username)
        if existin_user:
            raise ValidationError('Account with this username already exists!')
        
        if password != password2:
            raise ValidationError('The two password did not match!')
            # print('The two did not match!')
        return super(RegisterForm, self).clean()
