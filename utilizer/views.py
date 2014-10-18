from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import random

from .models import Article, User

# Create your views here.
def index(request):
	return HttpResponse("Hello World. You are at the index.")


def getRandomArticle(request, time)
	a_list = Article.objects.filter(timeToRead = time)
	a_choice = random.choice(a_list)
	context = {'randomArticle': a_choice}
	return render(request, #htmltemplatehere, context)


