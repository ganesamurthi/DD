from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.
class Subscriber(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length =254, unique=True)
    mobile = models.CharField(max_length =10, unique=True)
    updated = models.DateTimeField(auto_now=True)
    tiemstamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
