from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), help_text='password', label='Password')

    class Meta:
        model = User
        fields = ('username', 'password', 'email',)
