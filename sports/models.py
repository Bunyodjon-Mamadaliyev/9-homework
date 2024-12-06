from django.db import models


class Sports(models.Model):
    event_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    date = models.DateField()
    sport_type = models.CharField(max_length=100)
