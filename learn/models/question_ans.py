
from django.db import models
from .levels import Level
from .levels import Level

# Create your models here.

class Question(models.Model):
    que = models.CharField(max_length=1000)
    ans1 = models.CharField(max_length=100)
    ans2 = models.CharField(max_length=100)
    ans3 = models.CharField(max_length=100)
    ans4 = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100, default='')
    levels = models.ForeignKey(Level,on_delete=models.CASCADE,default=1)



    @staticmethod
    def get_all_questions():
        return Question.objects.all()

    
    @staticmethod
    def get_all_q_a(levels_id):
        if levels_id:
            return Question.objects.filter(levels = levels_id)
        else:
            return Question.objects.all()



