from django import forms
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from .models import *



class reserve_Form(forms.ModelForm):
    class Meta:
        model = reserveDesk
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(reserve_Form, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(label=('تاریخ'), 
            widget=AdminJalaliDateWidget 
        )
        

class Employe_Form(forms.ModelForm):
    class Meta:
        model = Emoloye
        fields = '__all__'
        
        
        
        

class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)    
    
    class Meta:
        model = registerModel
        fields = ['first_name','username','password']



class order_Form(forms.ModelForm):
    class Meta:
        model = order
        fields = ['phone','addres','paymentToAddres']
    