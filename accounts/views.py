from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('website:home')

        form = AuthenticationForm()
    else:
        return redirect('website:home')
    return render(request,"accounts/login.html", {"form":form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('website:home')

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,"You signup successful.")
            return redirect('website:home')
        else:
            messages.error(request,"Your password is too week.")
    else:
        form = UserCreationForm()
    return render(request,"accounts/signup.html", {"form":form})
