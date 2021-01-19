from django.shortcuts import render
from django.http import HttpResponse
from .models import Question



# from .models import question


# Create your views here.

def index(request):
    questions = Question.get_all_questions()
    set1 = questions[0:5]
    
    return render(request, 'index.html',{'questions':set1})





def index2(request):
    questions = Question.get_all_questions()
    set2 = questions[5:10]
    
    return render(request, 'index2.html',{'questions':set2})