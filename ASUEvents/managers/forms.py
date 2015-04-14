from django import forms
from django.core import validators 
from managers.models import Manager


class ManagerForm(forms.ModelForm):
    managerid = forms.CharField(max_length=25, label='Manager ID', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'form_control_1'}))
    fname = forms.CharField(max_length=35, label='First Name', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'form_control_1'}))
    mname = forms.CharField(max_length=35, label='Middle Name', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'form_control_1'}))
    lname = forms.CharField(max_length=35, label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'form_control_1'}))
    email = forms.EmailField(max_length=254, label='Email', validators=[validators.EmailValidator(message='Please enter a valid email address')], widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'form_control_1'}))
    sex = forms.CharField(max_length=1, label='Gender', widget=forms.Select(choices=(('', ''), ('m', 'Male'), ('f', 'Female')), attrs={'class': 'form-control', 'id': 'form_control_1'}))

    class Meta:
        model = Manager
        fields = ('managerid', 'fname', 'mname', 'lname', 'sex',)
