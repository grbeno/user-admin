from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Rendering home page of start
def homePageView(request):
  return render(request, 'start/home.html')

# Rendering start page
@login_required
def startPageView(request):
  return render(request, 'start/start.html')