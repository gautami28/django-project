from django import forms
from django.forms import fields,widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100,label="enter your search:")

class ConversionForm(forms.Form):
    CHOICES = [('length','Length'),('mass','Mass'),('time',"Time")]
    measurement = forms.ChoiceField(choices = CHOICES , widget=forms.RadioSelect)

class ConversionLengthForm(forms.Form):
    CHOICES = [('yard','Yard'),('foot','Foot'),('meter','Meter'),('centimeter','Centimeter')]
    input = forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs = {'type':'number','placeholder':'Enter the Number'}
    ))
    measure1 = forms.CharField(
        label = '',widget = forms.Select(choices = CHOICES)
    )
    measure2 = forms.CharField(
        label = '',widget = forms.Select(choices = CHOICES)
    )
    measure3 = forms.CharField(
        label = '',widget = forms.Select(choices = CHOICES)
    )
    measure4 = forms.CharField(
        label = '',widget = forms.Select(choices = CHOICES)
    )
class ConversionMassForm(forms.Form):
    CHOICES = [('pound','Pound'),('kilogram','Kilogram'),('gram','Gram')]
    input = forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs = {'type':'number','placeholder':'Enter the Number'}
    ))
    measure1 = forms.CharField(
        label = '',widget = forms.Select(choices = CHOICES)
    )
    measure2 = forms.CharField(
        label = '',widget = forms.Select(choices = CHOICES)
    )
    measure3 = forms.CharField(
        label = '',widget = forms.Select(choices = CHOICES)
    )
    
class ConversionTimeForm(forms.Form):
    CHOICES = [('seconds','Seconds'),('minutes','Minutes'),('hours','Hours')]
    input = forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs = {'type':'number','placeholder':'Enter the Number'}
    ))
    measure1 = forms.CharField(
        label = '',widget = forms.Select(choices = CHOICES)
    )
    measure2 = forms.CharField(
        label = '',widget = forms.Select(choices = CHOICES)
    )
    measure3 = forms.CharField(
        label = '',widget = forms.Select(choices = CHOICES)
    )
    

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

