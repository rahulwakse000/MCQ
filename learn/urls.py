from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static

from .views import index


urlpatterns = [
    path('', index, name='homepage'),
    # path('base',base ,name='base1')
]