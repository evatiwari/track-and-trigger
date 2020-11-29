from django.shortcuts import render, redirect
from .models import UserData
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def signup(request):
  if request.method == 'POST':
    user_name = request.POST['user_name']
    phone_number = request.POST['phone_number']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    user = User.objects.create_user(username=user_name, email = email, password = password1)
    user.first_name= phone_number
    user.save()
    print("User created")
    return redirect('login')
  return render(request, 'signup.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['user_name']
    password = request.POST['password']
    user=authenticate(request,username = username, password=password)
    if user:
      login(request, user)
      return redirect('dashboard')
  return render(request, 'login.html')