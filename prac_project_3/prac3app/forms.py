from django import forms
from django.core import validators
from prac3app import models


def odd_or_even(values):
    if values%2==1:
        raise forms.ValidationError("Please enter Even Number !!")






class user_from(forms.Form):
    user_name=forms.CharField(label="Full Name", widget=forms.TextInput(attrs={'style':'height:20px'}),required=False,validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(4)])
    user_email=forms.CharField(label="User Email",widget=forms.TextInput(attrs={'placeholder':'Enater Your Email Address '}),required=False)
    user_vmail=forms.CharField(label="Verify Email ",widget=forms.TextInput(attrs={'palceholder': 'Enter Your Email Again '}))
    user_phone=forms.CharField(label="Mobile Number",max_length=11,min_length=3)
    user_dob=forms.DateField(label="Date Of Birth" ,widget=forms.TextInput(attrs={'type':'date'}),required=False)
    user_address=forms.CharField(label="Address",required=False)
    zone_choice=(('','--SELECT OPSTION--'),('1','Mirpur'),('2','Kadamtoli'),('3','Dania'))
    user_zone=forms.ChoiceField(choices=zone_choice)
    city=(('1','Dhaka'),('2','Cumillah'),('3','Sylhet'))

    user_city=forms.MultipleChoiceField(choices=city,widget=forms.CheckboxSelectMultiple)

    user_numb=forms.IntegerField(validators=[odd_or_even])



    def clean(self):
        all_cleaned_data=super().clean()
        user_email=all_cleaned_data['user_email']
        user_vmail=all_cleaned_data['user_vmail']

        if user_email!= user_vmail :
            raise forms.ValidationError("Email does not Match !!!")


class Player_list_form(forms.ModelForm):
    class Meta :
        model=models.Player
        fields="__all__"
