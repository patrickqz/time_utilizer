from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from datetime import date
import random
import json

from .models import Article, User

def index(request):
	template = loader.get_template('utilizer/index.html')
	context  = RequestContext(request, {'nothing' : 2})
	return HttpResponse(template.render(context))
# Create your views here.
# def index(request):
# 	return HttpResponse("Hello World. You are at the index.")

def getRandomArticle(request):
	a_list = Article.objects.filter(timeToRead = time)
	a_choice = random.choice(a_list)
	context = {'randomArticle': a_choice}
	return render(request, htmltemplatehere, context)

def login(request):
	#if request.method == "POST" and request.is_ajax():
	#	return HttpResponse("great success")
	json_response = {'user': 'derp'}
	return HttpResponse(json.dumps(json_response), content_type='application/json')


