from django import forms
from .models import User,Customers

class UserCreate(forms.ModelForm):
    class Meta:
        model=User
        fields=['fname','lname','email','mobile']
