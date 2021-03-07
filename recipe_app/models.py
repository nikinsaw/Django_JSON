from django.db import models


class Items(models.Model):
    title = models.CharField(max_length=50)
    calories = models.IntegerField()
    url = models.CharField(max_length=2083)
    description = models.CharField(max_length=2083, default="")
    time = models.IntegerField(default=0)
