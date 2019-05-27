from django import forms
from .models import User, Recipe, Cheff

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class CheffForm(forms.ModelForm):
    class Meta:
        model = Cheff
        fields = ()