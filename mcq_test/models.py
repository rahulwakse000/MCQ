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

    def get_all_questions():
        return Questions.objects.all()


class Answers_alll(models.Model):
    question_correct = models.CharField(max_length=500)
    answer_co = models.CharField(max_length=100, default='')


    def __str__(self):
        return self.question_correct


    def get_qus_ans():
        return Answers_alll.objects.all()