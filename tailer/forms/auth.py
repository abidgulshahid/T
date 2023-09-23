from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.ModelForm):
    username = forms.EmailField(max_length = 200, widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput(), max_length=255)

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args,  **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Your Email'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter Your Password'


class Signup(forms.ModelForm):
    username = forms.EmailField(max_length = 200, widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput(), max_length=255)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name','last_name']

    def __init__(self, *args, **kwargs):
        super(Signup, self).__init__(*args,  **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Your Email'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter Your Password'