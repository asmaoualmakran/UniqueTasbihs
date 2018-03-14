from django.db import models
from django.apps import apps


class ItemCategory(models.Model):

	categoryName = models.CharField(max_length=100, unique=True)
