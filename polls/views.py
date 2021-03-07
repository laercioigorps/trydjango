from django.shortcuts import render
from django.http  import HttpResponse
from .models import Question, Choice
# Create your views here.

def index(request):
	question_list = Question.objects.all()

	context = {

		"list_questions" : question_list,
	}
	return render(request, "polls/index.html", context)

def detail(request, question_id):
	question = Question.objects.get(id=question_id)

	choice_list = question.choice_set.all()

	context = {

		"list_choices" : choice_list,
		"question" : question,
	}
	return render(request, "polls/detail.html", context)

def vote(request, question_id):
	question = Question.objects.get(id=question_id)
	choice_id = question.choice_set.get(id= request.POST['choice'])
	return HttpResponse("sua escolha foi %s" % str(choice_id.id))