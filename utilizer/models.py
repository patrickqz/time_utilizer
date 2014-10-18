from django.db import models

# Create your models here.

class User(models.Model):
	#TODO: create user model

class Article(models.Model):
	url = models.charField(max_length = 200)
	date_added = models.DateTimeField('date added')
	title = models.CharField(max_length=200)
	user = models.ForeignKey(User)

	#optional
	tag = models.CharField(max_length=50)
	notes = models.TextField()

	def _str_(self):
		return self.title

