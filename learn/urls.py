from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static

from .views import get
from .views import get2




urlpatterns = [
    path('', get, name='index'),
    path('2',get2 ,name='index2'),
    
]