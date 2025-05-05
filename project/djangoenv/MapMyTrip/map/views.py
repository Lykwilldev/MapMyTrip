from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,logout, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models
from django.contrib import messages


def index(request):
    #profiles = Profile.objects.all()
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('login')  
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'sign-up-page/sign-up.html', context)
   
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')  
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')  
    else:
        return render(request, 'log-in-page/log-in.html')  

def logout_view(request):
    logout(request)
    return redirect('index')


def profile(request):
    profile = models.Profile.objects.get(id=1)
    
    context = {
        'profile': profile,
    }
    return render(request, 'profile-page/profile.html',context)
# Create your views here.
