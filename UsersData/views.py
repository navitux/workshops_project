from django.shortcuts import render,  redirect
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/signupin/')
def dashboard(request):
    return render(request,"UsersData/dashboard.html")

def create_course(request):
    pass
