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
        field = self.fields['user']
        field.widget = field.hidden_widget()
        self.fields['name'].required = False
        self.fields['phone_number'].required = False


    def clean_name(self):
        first_name = self.cleaned_data['name']
        regex = r"[A-Za-z\s]+"
        if first_name:
            if not re.search(regex, first_name):
                raise forms.ValidationError("Only Characters are allowed")
        return first_name

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        number_pattern = re.compile(r'\d+')
        if phone_number:
            if number_pattern.findall(phone_number):
                return phone_number
            raise forms.ValidationError("Only Numbers are allowed")
        return ""

    def clean_length(self):
        id_length = self.cleaned_data['length']
        number_pattern = re.compile(r'\d+')
        if id_length:
            if number_pattern.findall(id_length):
                return id_length
            raise forms.ValidationError("Only Numbers are allowed")
        return None

    def clean_waist(self):
        waist = self.cleaned_data['waist']
        number_pattern = re.compile(r'\d+')
        if waist:
            if number_pattern.findall(waist):
                return waist
            raise forms.ValidationError("Only Numbers are allowed")
        return None

    def clean_low_waist(self):
        low_waist = self.cleaned_data['low_waist']
        number_pattern = re.compile(r'\d+')
        if low_waist:
            if number_pattern.findall(low_waist):
                return low_waist
            raise forms.ValidationError("Only Numbers are allowed")
        return None

    def clean_hip(self):
        hip = self.cleaned_data['hip']
        number_pattern = re.compile(r'\d+')
        if hip:
            if number_pattern.findall(hip):
                return hip
            raise forms.ValidationError("Only Numbers are allowed")
        return None

    def clean_muscle(self):
        muscle = self.cleaned_data['muscle']
        number_pattern = re.compile(r'\d+')
        if muscle:
            if number_pattern.findall(muscle):
                return muscle
            raise forms.ValidationError("Only Numbers are allowed")
        return None

    def clean_arm_hole(self):
        arm_hole = self.cleaned_data['arm_hole']
        number_pattern = re.compile(r'\d+')
        if arm_hole:
            if number_pattern.findall(arm_hole):
                return arm_hole
            raise forms.ValidationError("Only Numbers are allowed")
        return None

    def clean_collar(self):
        collar = self.cleaned_data['collar']
        number_pattern = re.compile(r'\d+')
        if collar:
            if number_pattern.findall(collar):
                return collar
            raise forms.ValidationError("Only Numbers are allowed")
        return None

    def clean_pocket(self):
        pocket = self.cleaned_data['pocket']
        number_pattern = re.compile(r'\d+')
        if pocket:
            if number_pattern.findall(pocket):
                return pocket
            raise forms.ValidationError("Only Numbers are allowed")
        return None

    def clean_pancha(self):
        pancha = self.cleaned_data['pancha']
        number_pattern = re.compile(r'\d+')
        if pancha:
            if number_pattern.findall(pancha):
                return pancha
            raise forms.ValidationError("Only Numbers are allowed")
        return None

    def clean_payment(self):
        payment = self.cleaned_data['payment']
        number_pattern = re.compile(r'\d+')
        if payment:
            if number_pattern.findall(payment):
                return payment
            raise forms.ValidationError("Only Numbers are allowed")
        return None

    def clean_pant_length(self):
        pant_length = self.cleaned_data['pant_length']
        number_pattern = re.compile(r'\d+')
        if pant_length:
            if number_pattern.findall(pant_length):
                return pant_length
            raise forms.ValidationError("Only Numbers are allowed")
        return None

    def clean_pant_width(self):
        pant_width = self.cleaned_data['pant_width']
        number_pattern = re.compile(r'\d+')
        if pant_width:
            if number_pattern.findall(pant_width):
                return pant_width
            raise forms.ValidationError("Only Numbers are allowed")
        return None

    def clean_cloth_quantites(self):
        pant_width = self.cleaned_data['cloth_quantites']
        number_pattern = re.compile(r'\d+')
        if pant_width:
            if number_pattern.findall(pant_width):
                return pant_width
            raise forms.ValidationError("Only Numbers are allowed")
        return None

    def clean_cloth_price(self):
        id_length = self.cleaned_data['cloth_price']
        number_pattern = re.compile(r'\d+')
        if id_length:
            if number_pattern.findall(id_length):
                return id_length
            raise forms.ValidationError("Only Numbers are allowed")
        return None
