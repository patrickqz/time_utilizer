from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from datetime import date
import random

from .models import Article, User

def index(request):
	template = loader.get_template('utilizer/index.html')
	context  = RequestContext(request, {'nothing' : 2})
	return HttpResponse(template.render(context))
# Create your views here.
def index(request):
	return HttpResponse("Hello World. You are at the index.")

def login(request):
	

def getRandomArticle(request, time)
	a_list = Article.objects.filter(timeToRead = time)
	a_choice = random.choice(a_list)
	context = {'randomArticle': a_choice}
	return render(request, #htmltemplatehere, context)


