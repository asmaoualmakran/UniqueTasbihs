from django.db import models

class Discount(models.Model):
	percentage = models.IntegerField()