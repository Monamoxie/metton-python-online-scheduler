from django.http import HttpResponse
from django.contrib.auth import authenticate, login as authLogin, logout as authLogout
from django.contrib import messages
from django.shortcuts import redirect, render

from dashboard.models import User
from .forms import RegisterForm, LoginForm
from django.contrib.auth import get_user_model


# Create your views here.
def home(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # login
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                authLogin(request, user)
                messages.success(request, "Welcome on board!")
                return redirect("dashboard")
            else:
                messages.error(request, "No user was found")
                return redirect("home")
        else:
            messages.error(request, form.errors)
            return redirect("register")
    else:
        form = RegisterForm()
        return render(request, "authentication/register.html", {"form": form})


def logout(request):
    authLogout(request)
    messages.success(request, "Goodbye! See you soon")
    return redirect("home")


def login(request):
    if request.method == "POST":
        # login
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            authLogin(request, user)
            messages.success(request, "Welcome back")
            return redirect("dashboard")
        else:
            messages.error(request, "Email/Password is incorrect")
            return redirect("login")
    else:
        return render(request, "authentication/login.html")

