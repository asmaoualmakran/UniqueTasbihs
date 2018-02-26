from django.db import models
import datetime
from customer import Customer
from item import Item
from address import Address

class Order(models.Model):
	customer_id = models.ForeignKey(Customer, on_delete=PROTECT, null=False)
	item 		= models.ForeignKey(Item, on_delete=PROTECT, null=False)
	TAV			= models.ItegerField(null=False)
	discount	= models.ItegerField()
	delivery_address = models.ForeignKey(Address, on_delete=PROTECT, null=False)
	billing_address = models.ForeignKey(Address, on_delete=PROTECT, null=False)
	date = DateField((auto_now_add=True, editable=False)