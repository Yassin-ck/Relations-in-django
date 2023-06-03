from django.shortcuts import render
from .models import Departments,Employees 
from django.http import HttpResponse

# Create your views here.


def new_view(request):
    user=Employees.objects.filter(id=1)

    return HttpResponse(user)