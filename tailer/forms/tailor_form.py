from django.contrib.auth.models import User
from django import forms
from tailer.models import Tailor



class TailorForm(forms.ModelForm):
    class Meta:
        model = Tailor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TailorForm, self).__init__(*args,  **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"
            # self.fields[field].required = True
        self.fields['order_take'].widget = forms.TextInput(attrs={'type': 'date'})
        self.fields['order_take'].widget.attrs['class'] = "form-control"

        self.fields['order_deadline'].widget = forms.TextInput(attrs={'type': 'date'})
        self.fields['order_deadline'].widget.attrs['class'] = "form-control"

    # def clean_phone_number(self):
