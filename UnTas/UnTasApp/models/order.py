from django.db import models
import datetime
from customer import Customer
from item import Item
from address import Address

class Order(models.Model):
	customer_id = models.ForeignKey(Customer, on_delete=PROTECT, null=False)
	item_id 		= models.ForeignKey(Item, on_delete=PROTECT, null=False)
	TAV			= models.IntegerField(null=False)
	discount	= models.IntegerField()
	price_total = models.IntegerField()
	delivery_address = models.ForeignKey(Address, on_delete=PROTECT, null=False)
	billing_address = models.ForeignKey(Address, on_delete=PROTECT, null=False)
	date = models.DateField((auto_now_add=True, editable=False)