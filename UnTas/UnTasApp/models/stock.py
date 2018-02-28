from django.db import models
from item import Item

class Stock(models.Model):
	item_id = models.ForeignKey(Item, null=False, unique=True)
	amount	= models.IntegerField(default=0)