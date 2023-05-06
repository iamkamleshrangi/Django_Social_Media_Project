from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from media_app.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@csrf_exempt
def sign_up(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            print("username already taken")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            print("email already taken")
            return redirect('signup')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user = auth.authenticate(username=username, password=password)
        if user:
            # User is authenticated
            auth.login(request, user)
            return JsonResponse({"message" : "sign up"})
        else:
            print("some error is there")
    else:
        print("return sign up html page")
        
@csrf_exempt
def sign_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user:
            # binding
            auth.login(request, user)
            return JsonResponse({"message" : "sign in"})
            
        else:
            print("Some error is there")
    else:
        print("get method for sign in")
        print("render sign in  html page")

@csrf_exempt
def sign_out(request):
     # opposite of binding
    auth.logout(request)
    return JsonResponse({"message" : "sign out"})
    
@login_required(login_url='sign_in')
def profile_settings(request):
    try:
        response_data = {
            "message" : "Hello, you are at profile settings page with current details",
            "id": request.user.id,
            "email": request.user.email,
            "username": request.user.username
        }
        return JsonResponse(response_data)
    except:
        return JsonResponse({"message" : "you are already signed out"})
        
