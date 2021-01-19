from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Question
from django.views import View


# from .models import question


# Create your views here.
class QusAns1(View):
    def get(self,request):
        # que1 = Question.get_all_que()
        questions = Question.get_all_questions()
        set1 = questions[0:5]
        
        categoryID = request.GET.get('question'[1])
        
        print(set1[0:5])

        return render(request, 'index.html', {'questions': set1})


class QusAns2(View):
    def get(self,request):
        questions = Question.get_all_questions()
        set2 = questions[5:10]

        return render(request, 'index2.html', {'questions': set2})


class QusAns3(View):
    def get(self,request):
        questions = Question.get_all_questions()
        set3 = questions[10:15]

        return render(request, 'index3.html', {'questions': set3})


class QusAns4(View):
    def get(self,request):
        questions = Question.get_all_questions()
        set4 = questions[15:20]

        return render(request, 'index4.html', {'questions': set4})
