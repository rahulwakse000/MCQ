from django.http.request import HttpHeaders
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .models.levels import Level
from .models.question_ans import Question
from .models.levels import Level





# Create your views here.

def get(request):
    
    questions = Question.get_all_questions()
    levels = Level.get_all_level()
    set1 = questions[0]
    set2 = questions[1]
    set3 = questions[2]
    set4 = questions[3]
    set5 = questions[4]

    


    # print(questions[0].id)
    # print(request.method)

    if request.method == 'GET':
        return render(request, 'index.html',{'set1':set1,'set2':set2,'set3':set3,'set4':set4,'set5':set5})
    elif request.method == 'POST':
        postData = request.POST

        option1 = postData.get('')
        option2 = postData.get('opt2')
        option3 = postData.get('opt3')
        option4 = postData.get('opt4')

        print(option1,option2,option3,option4)
        return HttpResponse(request.POST.get('opt1'))

    








def get2(request):
    questions = Question.get_all_questions()
    set6 = questions[5]
    set7 = questions[6]
    set8 = questions[7]
    set9 = questions[8]
    set10 = questions[9]

    return render(request, 'index2.html',{'set6':set6,'set7':set7,'set8':set8,'set9':set9,'set10':set10})

    
