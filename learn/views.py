from django.shortcuts import render
from django.http import HttpResponse
from .models import Question



# from .models import question


# Create your views here.

def index(request):
    questions = Question.get_all_questions()
    
    return render(request, 'index.html',{'questions':questions})





def base(request):
    
    return render(request, 'index2.html')