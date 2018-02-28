from django.db import models
from item import Item

class ItemCategory(models.Model):

	categoryName = models.CharField(max_length=100, unique=True)
	item_id = models.ForeignKey(Item, on_delete=models.CASCADE)