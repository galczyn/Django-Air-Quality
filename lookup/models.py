from django.db import models

class Station(models.Model):
    id = models.IntegerField(primary_key=True)
    station_name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
