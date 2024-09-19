from django.db import models


class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    localtime = models.DateTimeField(null=True, blank=True)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    condition = models.CharField(max_length=100, null=True, blank=True) 
    wind_speed = models.FloatField(null=True, blank=True) 
    pressure = models.FloatField(null=True, blank=True) 
    timestamp = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.city} | {self.temperature}°C | {self.humidity}% | {self.timestamp}"
