from django.db import models
from UnTasApp.models.item import Item

class Stock(models.Model):
	item_id = models.OneToOneField(Item, null=False, on_delete=models.PROTECT)
	amount	= models.IntegerField(default=0)