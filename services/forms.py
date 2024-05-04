from django import forms
from .models import User, Order

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone', 'email']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['service']