from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order

class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    first_name=forms.CharField(max_length=60,required=True)
    class Meta:
        model=User
        fields=('username','first_name','email','password1','password2')

class CheckoutForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=('full_name','email','phone','address','city','pincode')
        widgets={'address':forms.Textarea(attrs={'rows':3})}
