from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
#from .serializers import InventorySerializer
from rest_framework.response import Response
from rest_framework import status
from login.models import UserData
from django.contrib.auth import authenticate, login, logout
from .models import Item
# Create your views here.
@login_required
def dashboard(request):
  return render(request, 'index.html',{'user': request.user})

@login_required
def userprofile(request):
  return render(request, 'userprofile.html')


@login_required
def track(request):
  if request.method == 'POST':
    name = request.POST['name']
    quantity = request.POST['quantity']
    username = request.user.username
    item= Item.objects.create(name = name, quantity = quantity, username = username)
    item.save()
  return render(request, 'track.html')

@login_required
def tracklist(request):
  items = Item.objects.filter(username__contains = request.user.username)
  return render(request, 'tracklist.html', {'items':items})

@login_required
def trigger(request):
  return render(request, 'trigger.html')

@login_required
def logout(request):
  logout(request)
  return redirect('login')