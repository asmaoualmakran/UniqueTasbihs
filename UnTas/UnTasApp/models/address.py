from django.db import models

class Address(models.Model):

	street = CharField(max_length=100)
	number = CharField(max_length=20)
	zip_code = CharField(max_length=10)
	city = CharField(max_length=100)
	country = CharField(max_length=100)

