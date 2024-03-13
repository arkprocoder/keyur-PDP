from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def signup(request):
    if request.method=="POST":
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        confirmpass=request.POST.get('pass2')
        print(email,pass1,confirmpass)
        print("Post request is hitted")
    return render(request,"signup.html")

def handleLogin(request):
    return render(request,"login.html")

def handleLogout(request):
    return render(request,"login.html")