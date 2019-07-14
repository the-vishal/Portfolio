from django.db import models

# Create your models here.

class Project(models.Model):
	image = models.ImageField(upload_to='images/')
	name = models.CharField(max_length=50)
	summary = models.CharField(max_length =200)
	link = models.CharField(max_length=200, default=0)

	def __str__(self):
		return self.name