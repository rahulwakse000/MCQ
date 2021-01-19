from django.contrib import admin
from .models.question_ans import Question 
from .models.levels import Level


# Register your models here.

admin.site.register(Question)
admin.site.register(Level)
