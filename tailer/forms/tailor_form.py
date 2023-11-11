from django.contrib.auth.models import User
from django import forms
from tailer.models import Customer
import re


class TailorForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TailorForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"
            self.fields[field].required = False
        self.fields['order_take'].widget = forms.TextInput(attrs={'type': 'date'})
        self.fields['order_take'].widget.attrs['class'] = "form-control"

        self.fields['order_deadline'].widget = forms.TextInput(attrs={'type': 'date'})
        self.fields['order_deadline'].widget.attrs['class'] = "form-control"

        self.fields['name'].required = True
        self.fields['phone_number'].required = True

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        number_pattern = re.compile(r'\d+')
        if number_pattern.findall(phone_number):
            return  phone_number
        raise forms.ValidationError("Only Numbers are allowed")

    def clean_length(self):
        id_length = self.cleaned_data['length']
        number_pattern = re.compile(r'\d+')
        if id_length and number_pattern.findall(id_length):
            return id_length
        raise forms.ValidationError("Only Numbers are allowed")


    def clean_waist(self):
        waist = self.cleaned_data['waist']
        number_pattern = re.compile(r'\d+')
        if waist and number_pattern.findall(waist):
            return waist
        raise forms.ValidationError("Only Numbers are allowed")


    def clean_low_waist(self):
        low_waist = self.cleaned_data['low_waist']
        number_pattern = re.compile(r'\d+')
        if low_waist and number_pattern.findall(low_waist):
            return low_waist
        raise forms.ValidationError("Only Numbers are allowed")


    def clean_hip(self):
        hip = self.cleaned_data['hip']
        number_pattern = re.compile(r'\d+')
        if hip and number_pattern.findall(hip):
            return hip
        raise forms.ValidationError("Only Numbers are allowed")


    def clean_muscle(self):
        muscle = self.cleaned_data['muscle']
        number_pattern = re.compile(r'\d+')
        if muscle and number_pattern.findall(muscle):
            return muscle
        raise forms.ValidationError("Only Numbers are allowed")


    def clean_arm_hole(self):
        arm_hole = self.cleaned_data['arm_hole']
        number_pattern = re.compile(r'\d+')
        if arm_hole and number_pattern.findall(arm_hole):
            return arm_hole
        raise forms.ValidationError("Only Numbers are allowed")

    def clean_collar(self):
        collar = self.cleaned_data['collar']
        number_pattern = re.compile(r'\d+')
        if collar and number_pattern.findall(collar):
            return collar
        raise forms.ValidationError("Only Numbers are allowed")

    def clean_pocket(self):
        pocket = self.cleaned_data['pocket']
        number_pattern = re.compile(r'\d+')
        if pocket and number_pattern.findall(pocket):
            return pocket
        raise forms.ValidationError("Only Numbers are allowed")


    def clean_pancha(self):
        pancha = self.cleaned_data['pancha']
        number_pattern = re.compile(r'\d+')
        if pancha and number_pattern.findall(pancha):
            return pancha
        raise forms.ValidationError("Only Numbers are allowed")


    def clean_payment(self):
        payment = self.cleaned_data['payment']
        number_pattern = re.compile(r'\d+')
        if payment and number_pattern.findall(payment):
            return payment
        raise forms.ValidationError("Only Numbers are allowed")


