from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static

from .views import index, index2,index3,index4



urlpatterns = [
    path('', index, name='index'),
    path('2',index2 ,name='index2'),
    path('3',index3 ,name='index3'),
    path('4',index4 ,name='index4'),
]