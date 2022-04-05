from django.shortcuts import render,  redirect
from Courses.models import *
from django.contrib.auth.models import User
from django.contrib import auth
from Courses import views
from django.contrib.auth.decorators import login_required
# Create your views here.
# Function to redirect the user to Login and Sign up page.
def signupin(request):
    return render(request,"SignUpIn/signupin.html")

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username_r'])
                return render(request, 'SignUpIn/signupin.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username_r'],
                                                password=request.POST['password1'],
                                                email=request.POST['email'],
                                                first_name=request.POST['firstname'],
                                                last_name=request.POST['lastname'])
                auth.login(request,user)
                return redirect('index')
        else:
            return render(request, 'SignUpIn/signupin.html', {'error':'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'SignUpIn/signupin.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'SignUpIn/signupin.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'SignUpIn/signupin.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')

@login_required(login_url='/signupin/')
def delete_user_completely(request):
    ''' This view is to delete completely a user account with all courses related to this account '''
    
    pass
