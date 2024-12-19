from django.contrib import admin

# Register your models here.
from .models import Exam,QuizResult

admin.site.register(Exam)
admin.site.register(QuizResult)