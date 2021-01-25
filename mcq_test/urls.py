from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from .views.index import index
from .views.mark import mark

from .views.login import Login



urlpatterns = [
    path('',Login.as_view(), name='login'),
    path('2',index,name='homepage'),
    path('result',mark,name='mark')
]