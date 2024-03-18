from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def signup(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        confirmpass=request.POST.get('pass2')
        if pass1 != confirmpass:
            messages.error(request,"Password do not match")
            return redirect('/signup/')
        # handling integrity error
        try:
            if User.objects.get(username=email):
                messages.warning(request,"Email Already Taken")
                return redirect('/signup/')
        except:
            pass
        user = User.objects.create_user(email,email,pass1)
        user.first_name=fname
        user.last_name=lname
        user.save()
        messages.success(request,"Signup Success Please Login")
        return redirect('/login/')
        # print(email,pass1,confirmpass)
        # print("Post request is hitted")
    return render(request,"signup.html")

def handleLogin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        user=authenticate(username=email,password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login/')


    return render(request,"login.html")

def handleLogout(request):
    logout(request)
    messages.success(request,"Logout Success")
    return render(request,"login.html")