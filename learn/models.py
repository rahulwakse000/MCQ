from django.db import models

# Create your models here.

class Question(models.Model):
    que = models.CharField(max_length=1000)
    ans1 = models.CharField(max_length=100)
    ans2 = models.CharField(max_length=100)
    ans3 = models.CharField(max_length=100)
    ans4 = models.CharField(max_length=100)
    

class Answers(models.Model):
    correct_answer = models.CharField(max_length=100, default='')