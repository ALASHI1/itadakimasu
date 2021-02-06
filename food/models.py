from django.db import models

# Create your models here.
class Food(models.Model):
	title=models.CharField(max_length=200 , null=True)
	steps=models.CharField(max_length=7000 , null=True)
	ingredients=models.CharField(max_length=5000 , null=True)
	food_id = models.CharField(max_length=200 , null=True)
	image=models.CharField(max_length=200 , null=True)

