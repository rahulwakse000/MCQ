from django import views
from django.core.checks.messages import Error
from django.db.models.query_utils import PathInfo
from django.shortcuts import redirect, render
from django.http import HttpResponse
from mcq_test.models import User
from django.views import View


class Login(View):

    def get(self, request):

        print(request.method)
        return render(request, 'login.html')

    def post(self, request):
        print(request.method)

        postData = request.POST

        name = postData.get('name')
        phone = postData.get('phone')
        # validation

        value = {
            'name': name,
            'phone': phone
        }
        error_message = None

        user = User(name=name, phone=phone)

        error_message = self.validateUser(user)

        if not error_message:
           
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'login.html', data)

    def validateUser(self, user):
        error_message = None
        if(not user.name):
            error_message = "First Name Reqaired !"
        elif len(user.name) < 2:
            error_message = "First Name must be 2 char long or more"
        elif not user.phone:
            error_message = "Phone Number required"
        elif len(user.phone) < 10:
            error_message = "Phone Number must be 10 char Long"

        return error_message
