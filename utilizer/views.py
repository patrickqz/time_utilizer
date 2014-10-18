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

def login(request):
	#if request.method == "POST" and request.is_ajax():
	#	return HttpResponse("great success")
	json_response = {'user': 'derp'}
	return HttpResponse(json.dumps(json_response), content_type='application/json')
	# if request.method == 'POST':
	# 	#redirect to results page
	# 	return HttpResponseRedirect(reverse(views.getResult))
	# else:
	# 	return HttpResponse("Hello World. You are at the index.")



def addLink(request):
	if request.method == 'POST':
		title = request.POST['title']
		url = request.POST['url']
		timeToRead = request.POST['time']
		tag = request.POST['tag']

		#create Article and save it in database
		a = Article(title= title, url = url, timeToRead = timeToRead, 
			tag = tag, date_added = datetime.now())
		a.save()

		return HttpResponseRedirect("Thanks for submitting a link!")
	else: 

		return render(request, 'addLink.html')


def getResult(request):
	try: 
		a_list = Article.objects.filter(timeToRead = request.POST['time'], tag = request.POST['tag'])
	except not a_list:
		raise Http404
	
	a_choice = random.choice(a_list)
	context = {'randomArticle': a_choice}
	return render(request, "result.html", context)


