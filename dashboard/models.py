from django.db import models

# Create your models here.

class Inventory(models.Model):
    u_id = models.UUIDField(primary_key=True, editable=False)

class Item(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    item_name = models.CharField(max_length = 15)
    item_quantity = models.IntegerField()


