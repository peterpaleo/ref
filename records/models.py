from django.db import models

class Record(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	part1 = models.CharField(max_length=200)
	part2 = models.CharField(max_length=200)
	part3 = models.CharField(max_length=200)
	part4 = models.CharField(max_length=200)
	def __str__(self):
		return self.first_name + " " + self.last_name
