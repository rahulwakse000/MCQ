from django import views
from django.core.checks.messages import Error
from django.db.models.query_utils import PathInfo
from django.shortcuts import redirect, render
from django.http import HttpResponse



def mark(request):
    return render(request, 'mark.html')