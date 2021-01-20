from django.db.models.query_utils import PathInfo
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Questions, Answers_alll

# Create your views here.


def index(request):

    questions = Questions.get_all_questions()
    answer = Answers_alll.get_qus_ans()

    que0 = questions[0]
    que1 = questions[1]
    que2 = questions[2]
    que3 = questions[3]

    questions_list = [que0.answer, que1.answer, que2.answer, que3.answer]

    for i in questions_list:
        print(i)

    # print(questions)
    print(request.method)
    mark = []
    if request.method == 'POST':
        postData = request.POST
        opt = postData.get('quesiton')

        if questions_list[0] == opt:
            mark.append(5)
            print(mark)
        print(opt)

        return redirect('homepage')

    else:
        return render(request, 'index.html', {'qus_ans0': que0, 'qus_ans1': que1, 'qus_ans2': que2, 'qus_ans3': que3})
