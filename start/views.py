from django.shortcuts import render

# Rendering home page of start
def homePageView(request):
  return render(request, 'start/home.html')