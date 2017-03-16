from django.contrib import admin
from . import models
# Register your models here.

class AdminQuestion(admin.ModelAdmin):
	search_fields=('question_text',)
	list_display=('question_text','pub_date')

class ChoiceAdmin(admin.ModelAdmin):
	list_display=('question','choice_text','votes')
	search_fields=('question',)

		
admin.site.register(models.Question,AdminQuestion)
admin.site.register(models.Choice,ChoiceAdmin)