from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from .views import QusAns1,QusAns2,QusAns3,QusAns4
# from .views import index, index2,index3,index4



urlpatterns = [
    path('', QusAns1.as_view(), name='index'),
    path('2',QusAns2.as_view() ,name='index2'),
    path('3',QusAns3.as_view() ,name='index3'),
    path('4',QusAns4.as_view() ,name='index4'),
]