from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
  return render(request, 'index.html')

@login_required
def userprofile(request):
  return render(request, 'userprofile.html')

@login_required
def track(request):
  return render(request, 'track.html')

@login_required
def trigger(request):
  return render(request, 'trigger.html')