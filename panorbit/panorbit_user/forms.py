from django import forms                
from .models import PanorbitUser

class EditForm(forms.ModelForm):

    GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others')
)


    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':"First Name",
        }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':"Last Name",
        }))

    father_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':"Father's Name",
        }))

    phonenumber = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':"Phone No",
        }))

    email=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':"Email Id",
        }))

    gender = forms.ChoiceField(widget=forms.Select(attrs={
        'class':'form-control'

        }), choices=GENDER_CHOICES)


    spouse_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':"Spouse Name",
        }))

    password = forms.CharField(required=False, widget=forms.PasswordInput)

    class Meta:
        model = PanorbitUser
        fields = ('first_name', 'last_name','father_name','gender','email','phonenumber','spouse_name') 

 


class IndexForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':"Email Address",
        }))

class SignInForm(forms.Form):
    otp = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':"Enter OTP",
        }))