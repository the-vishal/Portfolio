from django.db import models
from datetime import datetime
# Create your models here.

class Project(models.Model):
	image = models.ImageField(upload_to='images/', default='images/default_project.gif')
	name = models.CharField(max_length=50)
	summary = models.CharField(max_length =200)
	link = models.CharField(max_length=200, default='#')
	date = models.DateTimeField(default=datetime.now(), blank=True)
	def __str__(self):
		return self.name