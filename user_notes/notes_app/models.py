from django.db import models

class OneNote(models.Model):
	title = models.CharField(max_length=200)
	note = models.CharField(max_length=500)
	author = models.ForeignKey('auth.User')


	def __str__(self):
		return self.title

