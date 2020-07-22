from django.shortcuts import render
from django.http import HttpResponse
from prac3app.models import Player,PlayerDetails
from prac3app import forms

# Create your views here.

def index(request):
    player_list=Player.objects.order_by('first_name')
    playerdetails=PlayerDetails.objects.order_by('fifa_rating')
    diction={'heading': 'List Of Players', 'playerlist':player_list,'pd':playerdetails }

    return render(request,'prac3app/index.html',context=diction)



def form(request):

    new_user_from=forms.user_from()

    dictions={
    'test_from':new_user_from,'heading':'From Using Django'

    }

    if request.method=="POST":
        new_from_sr=forms.user_from(request.POST)
        dictions.update({'test_from':new_from_sr})

        if new_from_sr.is_valid():
            sr_user_name=new_from_sr.cleaned_data['user_name']

            sr_user_dob=new_from_sr.cleaned_data['user_dob']
            sr_user_phone=new_from_sr.cleaned_data['user_phone']
            sr_user_address=new_from_sr.cleaned_data['user_address']

            sr_user_zone=new_from_sr.cleaned_data['user_zone']
            sr_user_city=new_from_sr.cleaned_data['user_city']
            sr_user_num=new_from_sr.cleaned_data['user_numb']

            dictions.update({'user_name':sr_user_name})
            dictions.update({'user_email':'Email Matched'})
            dictions.update({'user_dob':sr_user_dob})
            dictions.update({'user_phone':sr_user_phone})
            dictions.update({'user_address':sr_user_address})
            dictions.update({'user_zone':sr_user_zone})
            dictions.update({'user_city':sr_user_city})
            dictions.update({'user_numb':sr_user_num})

            dictions.update({'form_submit':"YES"})

    return render(request,'prac3app/form.html',context=dictions)




def signup_forms(request):
     player_list=forms.Player_list_form()
     if request.method=="POST":
         player_list=forms.Player_list_form(request.POST)

         if player_list.is_valid():
             player_list.save(commit=True)
             return index(request)



     dictions={'signup':player_list,'text2':"ADD NEW PLAYER TO THE LIST"}
     return render(request,'prac3app/signup.html',context=dictions)
