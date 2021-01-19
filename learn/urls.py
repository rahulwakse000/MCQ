from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static

from .views import index
from .views import index2


urlpatterns = [
    path('', index, name='index'),
    path('2',index2 ,name='index2')
]