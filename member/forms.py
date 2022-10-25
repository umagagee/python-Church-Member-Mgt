from .models import *
from django.forms import ModelForm,widgets
from django import forms




class memberForm(forms.ModelForm):
    
    class Meta:
        model  = Member 
        fields ='__all__'
        gender=(('male','male'),('female','female'),('other','other'))
        level = (('Professor','Professor'),
    ('Masters','Masters'),('Degree','Degree'),
    ('High School','High School'),('Others','Others'))
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter firstname'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter lastname'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'name@Example.com','type':'email'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Number','type':'tel'}),
            'sex':forms.Select(attrs={'class':'form-control'},choices=gender),
            'birth_date':forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'age':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'Occupation':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Occpation'}),
            'education':forms.Select(attrs={'class':'form-control'},choices=level),
            'Address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Address'}),
            'date_join':forms.TextInput(attrs={'class':'form-control','type':'date'})
        }

class paymentForm(ModelForm):
    class Meta:
        model  = Payment
        fields = '__all__'
        catergory = (('Tithe','Tithe'),('Contribution','Contribution'),
    ('Collection','Collection'),('Dues','Dues'),
    ('Others','Others'))

        method = (('Cash','Cash'),('Cheque','Cheque'),
        ('Card','Card'),('Mobile Money','Mobile Money'),
        ('Others','Others'))
        widgets = {
            'member':forms.Select(attrs={'class':'form-control'}),
            'amount':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'payment_cart':forms.Select(attrs={'class':'form-control'},choices=catergory),
            'payment_method':forms.Select(attrs={'class':'form-control'},choices=method),
            'date_paid':forms.TextInput(attrs={'class':'form-control','type':'date'})

            }

