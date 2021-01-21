from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from .views import index
from .views import login_index



urlpatterns = [
    path('',login_index, name='login'),
    path('2',index,name='homepage'),
    
]