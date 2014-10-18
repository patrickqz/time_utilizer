from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import random

from .models import Article, User

# Create your views here.
def index(request):
	if request.method == 'POST':
		#redirect to results page
		return HttpResponseRedirect(reverse(views.getResult))
	else:
		return HttpResponse("Hello World. You are at the index.")



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


