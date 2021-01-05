from django.shortcuts import render,  redirect
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/signupin/')
def dashboard(request):
    #Function only to show the dashboard page.
    return render(request,"UsersData/dashboard.html")

def create_coursetype(request):
    pass

def create_course(request):
    pass
