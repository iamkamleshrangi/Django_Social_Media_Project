from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from media_app.models import User

# Create your views here.
def sign_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            print("user is logged in", user)
        else:
            print("Some error is there")
    else:
        print("get method for sign in")