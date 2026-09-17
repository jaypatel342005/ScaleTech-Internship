from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate



# Create your views here.

def login_user(request):

    username = request.POST.get("username")
    password = request.POST.get("password")
    if request.method == "POST":
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username not found")
            return render(request, "login_user.html")
        user = authenticate(username=username, password=password)
        if not user:
            messages.error(request, "Incorrect password")
            return render(request, "login_user.html")
        login(request, user)
        return redirect("/")
    return render(request, "login_user.html")

def logout_user(request):
    logout(request)
    return redirect("/")

def register_user(request):

    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    retype_password = request.POST.get("retype_password")
    
    if request.method == "POST":
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, "register_user.html")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request, "register_user.html")
        if password != retype_password:
            messages.error(request, "Passwords do not match")
            return render(request, "register_user.html")
        user = User.objects.create_user(
            username=username,
            email=email,
            password=request.POST.get("password"),
        )
        login(request, user)
        return redirect("/")
    return render(request, "register_user.html")
