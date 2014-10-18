from django.db import models

# Create your models here.

class User(models.Model):
	#TODO: create user model
	name = models.charField(max_length=70)

class Article(models.Model):
	url = models.CharField(max_length = 200)
	date_added = models.DateTimeField('date added')
	title = models.CharField(max_length=200)
	user = models.ForeignKey(User)


	#optional
	timeToRead = models.IntegerField(blank=True)
	tag = models.CharField(blank=True, max_length=50)
	notes = models.TextField(blank=True)

	def _str_(self):
		return self.title



