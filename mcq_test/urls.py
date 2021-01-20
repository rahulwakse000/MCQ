from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from .views import index



urlpatterns = [
    path('',index,name='homepage'),
    # path('1',post_data)
    

]