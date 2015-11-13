from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=20)
	pub_date = models.DateTimeField('date published')
	isbn = models.CharField(max_length=14)
