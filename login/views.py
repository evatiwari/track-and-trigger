from django.shortcuts import render, redirect
from .models import UserData

# Create your views here.
def login(request):
  if request.method == 'POST':
    user_name = request.POST['user_name']
    phone_number = request.POST['phone_number']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    user = UserData.objects.create(user_name=user_name, phone_number=phone_number, email= email, password=password1)
    user.save()
    print("User created")
  return render(request, 'login.html')

