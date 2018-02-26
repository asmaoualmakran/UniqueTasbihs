from django.db import models

class Address(models.Model):

	street = models.CharField(max_length=100)
	number = models.CharField(max_length=20)
	zip_code = models.CharField(max_length=10)
	city = models.CharField(max_length=100)
	country = models.CharField(max_length=100)

