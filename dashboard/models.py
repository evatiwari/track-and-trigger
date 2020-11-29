from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=120)
    quantity = models.IntegerField(default = 0)
    username = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
