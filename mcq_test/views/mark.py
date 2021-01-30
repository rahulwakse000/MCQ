from django import views
from django.core.checks.messages import Error
from django.db.models.query_utils import PathInfo
from django.shortcuts import redirect, render
from django.http import HttpResponse
from mcq_test.models import User



def mark(request):
    user_data = User.get_all_user()
    first_user = user_data.last()
    name = first_user.name
    mark = first_user.mark
    data = {'name':name,'mark':mark}
    
    return render(request, 'mark.html',data)