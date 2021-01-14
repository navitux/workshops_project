from django.shortcuts import render,  redirect
from .models import CourseClass,Course
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/signupin/')
def dashboard(request):
    #Function only to show the dashboard page.
    return render(request,"UsersData/dashboard.html")

def create_courseclass(request):
    pass

def create_course(request):
    pass
