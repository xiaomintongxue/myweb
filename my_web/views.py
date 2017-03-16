from django.shortcuts import render,HttpResponse
from .models import Question

# Create your views here.
def detail(request,question_id):
	return HttpResponse("You're looking at question %s!" %question_id)


def index(request):
	latest_question_list=Question.objects.order_by('-pub_date')[:5]
	context={'latest_question_list':latest_question_list}
	return render(request,'index.html',context)
