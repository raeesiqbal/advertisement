from django.contrib.auth.models import Group
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import JsonResponse
from .models import *

def index(request):
    return HttpResponse("donefsffsff")

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("app1:home"))
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return HttpResponseRedirect(reverse("app1:home"))
        return render(
            request,
            "users/login.html",
            {"message": "invalid username/password"},
        )
    return render(request, "users/login.html")


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("app1:home"))


@login_required
def register_view(request):
    # can't register users if not the admin
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse("app1:home"))
    # if the request is post, this means that the form is filled.
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
        except IntegrityError:
            return render(
                request,
                "users/register.html",
                {"message": "Username is already taken", "message_type": "danger"},
            )
        # redirected to the login page when
        return render(
            request,
            "users/register2.html",
            {"message": "account successfully created", "message_type": "success"},
        )
    # if it is a get request, the register page will open
    return render(request, "users/register.html")