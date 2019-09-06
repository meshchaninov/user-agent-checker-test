# views.py
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import User
from .forms import RegisterForm, EditProfileForm


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST, response.FILES)
        if form.is_valid():
            form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(response, new_user)
            return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "registration/registration.html", {"form":form})

@login_required
def edit_profile(response):
    if response.method == "POST":
        form = EditProfileForm(response.POST, response.FILES, instance=response.user)
        if form.is_valid():
            form.save()
            return redirect("/accounts/profile")
    else:
        form = EditProfileForm(instance=response.user)
    return render(response, "registration/edit_profile.html", {"form":form})

@login_required
def profile(response):
    user = response.user
    return render(response, "registration/profile.html", {"user": user})

def profile_username(response, username):
    if username == response.user.username:
        return redirect(".")
    else:
        user = get_object_or_404(User, username=username)
        return render(response, "registration/profile_read_only.html", {"other_user": user})

def password_change_done(response):
    return render(response, "registration/password_change_done.html")