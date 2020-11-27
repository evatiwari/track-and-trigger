from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .serializers import InventorySerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@login_required
def dashboard(request):
  return render(request, 'index.html')

@login_required
def userprofile(request):
  return render(request, 'userprofile.html')

@login_required
def track(request):
  #return render(request, 'track.html')
  def post(self, request, *args, **kwargs):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.save()
            serializer = InventorySerializer(question)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required
def trigger(request):
  return render(request, 'trigger.html')