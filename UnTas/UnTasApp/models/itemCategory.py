from django.db import models
from django.apps import apps
from UnTasApp.models.item import Item

#Item = apps.get_model('item','Item')

class ItemCategory(models.Model):

	categoryName = models.CharField(max_length=100, unique=True)
	item_id = models.ForeignKey(Item, on_delete=models.CASCADE)