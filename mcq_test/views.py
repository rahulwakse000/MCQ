from django import views
from django.db.models.query_utils import PathInfo
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Questions
from django.views import View
# Create your views here.


def index(request):

    questions = Questions.get_all_questions()
    

    que0 = questions[0]
    que1 = questions[1]
    que2 = questions[2]
    que3 = questions[3]

    questions_list = [que0.answer, que1.answer, que2.answer, que3.answer]

    postData = request.POST
    opt1 = postData.get('quesiton1')
    opt2 = postData.get('quesiton2')
    opt3 = postData.get('quesiton3')
    opt4 = postData.get('quesiton4')

    print(request.method)
    mark = []
    if request.method == 'POST':

        if questions_list[0] == opt1:
            mark.append(5)
        if questions_list[1] == opt2:
            mark.append(5)
        if questions_list[2] == opt3:
            mark.append(5)
        if questions_list[3] == opt4:
            mark.append(5)

            print(sum(mark))
        return redirect('homepage')

    else:
        return render(request, 'index.html', {'qus_ans0': que0, 'qus_ans1': que1, 'qus_ans2': que2, 'qus_ans3': que3})


class Question_Answers(View):
    def get(self,**args):
        pass

