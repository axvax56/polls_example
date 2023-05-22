from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [('Question Statement', {'field' : ['question_text']}),
                 ('Date Information', {'fields' : ['pub_date'], 'classes':['collapse']})]