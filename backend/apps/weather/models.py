
from django.db import models
from apps.users.models import User

class WeatherData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    DateTime = models.DateTimeField()
    WeatherText = models.CharField(max_length=255)
    IsDayTime = models.BooleanField()
    Temperature = models.DecimalField(max_digits=5, decimal_places=2)
    Unit = models.CharField(max_length=10)
    country = models.CharField(max_length=250)
