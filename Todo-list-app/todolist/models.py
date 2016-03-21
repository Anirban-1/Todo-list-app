from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MyList(models.Model):
	task = models.CharField(max_length=100)
	priority = models.IntegerField(default=0)
	due_date = models.DateField()
	
	def __str__(self):
		return self.task
