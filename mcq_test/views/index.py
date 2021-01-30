from django import views
from django.db.models.query_utils import PathInfo
from django.shortcuts import redirect, render
from django.http import HttpResponse
from mcq_test.models import Questions
from mcq_test.models import User

from django.views import View
# Create your views here.



def index(request):
    

    questions = Questions.get_all_questions()
    mark_user1 = User.get_all_user()
    # print(mark_user1)
    # mark_user1.reverse()
    # print(mark_user1)
    # m1 = mark_user1[0].mark
    user = mark_user1.last()
    user_name = user.name
    print(user)
    
    que0 = questions[0]
    que1 = questions[1]
    que2 = questions[2]
    que3 = questions[3]
    link = {'qus_ans0': que0, 'qus_ans1': que1, 'qus_ans2': que2, 'qus_ans3': que3,'user':user_name}

    questions_list = [que0.answer, que1.answer, que2.answer, que3.answer]

    postData = request.POST

    opt1 = postData.get('quesiton1')
    opt2 = postData.get('quesiton2')
    opt3 = postData.get('quesiton3')
    opt4 = postData.get('quesiton4')
    print(request.method)
    mark_user = 0
    # print(request.session(;))
    
    
    
    if request.method == 'GET':
        
        
        return render(request, 'index.html',link )
        
    else:
        
        if questions_list[0] == opt1:
            mark_user = mark_user + 5
        else:
            pass
        if questions_list[1] == opt2:
            mark_user = mark_user + 5
        else:
            pass
        if questions_list[2] == opt3:
            mark_user = mark_user + 5
        else:
            pass
        if questions_list[3] == opt4:
            mark_user = mark_user + 5
        else:
            pass
        # mark = sum(mark_user)
        print(mark_user)
        user.mark = mark_user
        user.save()

        # m1.register()
        
        

        


        return redirect('mark')
         

        
    

