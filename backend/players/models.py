from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=256)
    sports = models.CharField(max_length=256)
    estimated_price=models.DecimalField(max_digits=15, decimal_places=2, default=50)