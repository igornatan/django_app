from django.db import models
from datetime import datetime

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    method = models.TextField()
    ingredients = models.TextField()
    category = models.TextField()
    prepare_time = models.IntegerField()
    production = models.CharField(max_length=100)
    creation_date = models.DateTimeField(default=datetime.now())
