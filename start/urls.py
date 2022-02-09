from django.urls import path
from .views import homePageView, startPageView


urlpatterns = [ path('', homePageView, name='home'),
                path('start/', startPageView, name='start'),  
            ]