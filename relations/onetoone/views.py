from django.shortcuts import render
from .models import Phone
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.


def my_view(request):
    ## Default way
    # user = User.objects.get(id=1)                 
    # phone = Phone.objects.get(user_id = user.id)   
    
    # Relation way
    user_phone1 = User.objects.get(id=1).no
    user = User.objects.get(id=1).no.user_id
    
    # print(user)
    # print(user_phone1)
    
    user2 = Phone.objects.get(id=1).user_id
    user2_phone = Phone.objects.get(id=1).phone_no
    # print(user2)
    # print(user2_phone)
    return HttpResponse(user2_phone)
   
    
    
    