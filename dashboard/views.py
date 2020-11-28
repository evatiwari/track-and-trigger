from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from .serializers import InventorySerializer
from rest_framework.response import Response
from rest_framework import status
from login.models import UserData

# Create your views here.
@login_required
def dashboard(request):
  if request.method == 'GET':
    username = request.GET.get('user_name')
    password = request.GET.get('password')
    user = UserData.objects.filter(user_name__contains=username, password__contains = password)
    print(u"User exists")

  return render(request, 'index.html')

def userprofile(request):
  return render(request, 'userprofile.html')
'''
def track(request):
  #return render(request, 'track.html')
  def post(self, request, *args, **kwargs):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            inventory = serializer.save()
            serializer = InventorySerializer(inventory)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
def track(request):
  return render(request, 'track.html')

def trigger(request):
  return render(request, 'trigger.html')