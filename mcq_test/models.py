
from django.db import models

# Create your models here.


class Questions(models.Model):
    quesiton = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)

    def __str__(self):
        return self.quesiton
        
    @staticmethod
    def get_all_questions():
        return Questions.objects.all()


class User(models.Model):
    name = models.CharField(max_length=100,default='user')
    phone = models.CharField(max_length=20)
    mark = models.CharField(max_length=10,default='0')


    
    def register(self):
        self.save()

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_user():
        return User.objects.all()
    @staticmethod
    def get_mark(mark):
        return User.objects.filter(mark = mark)