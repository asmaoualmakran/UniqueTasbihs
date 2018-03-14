from django.db import models



class ItemCategory(models.Model):
	categoryName = models.CharField(max_length=100, unique=True, null=False)
