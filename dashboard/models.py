from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Inventory(models.Model):
     user_name = models.CharField(primary_key = True, max_length = 15, blank = False, validators = [
        RegexValidator(regex='^[a-zA-Z0-9]*$', message = 'Username must be alphanumeric', code = 'invalid_username')
    ])

class Item(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    item_name = models.CharField(max_length = 15)
    item_quantity = models.IntegerField()


