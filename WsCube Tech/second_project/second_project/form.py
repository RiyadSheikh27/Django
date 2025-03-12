from django import forms

class UserForm(forms.Form):
    num1=forms.CharField()
    num2=forms.CharField()
