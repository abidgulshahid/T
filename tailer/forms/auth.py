from django.contrib.auth.models import User
from django import forms

from tailer.models import Users


class LoginForm(forms.Form):
    username = forms.EmailField(max_length = 200, widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput(), max_length=255)



    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args,  **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Your Email'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter Your Password'


class Signup(forms.ModelForm):
    username = forms.EmailField(max_length = 200, widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput(), max_length=255)
    CHOICES = (
      ('User', 'User'),
      ('Tailer', 'Tailer'),
      
  )
    type = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = Users
        fields = ['username', 'password', 'type']

    def __init__(self, *args, **kwargs):
        super(Signup, self).__init__(*args,  **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Your Email'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['type'].widget.attrs['class'] = 'form-control'
        # self.fields['first_name'].widget.attrs['class'] = 'form-control'
        # self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter Your Password'