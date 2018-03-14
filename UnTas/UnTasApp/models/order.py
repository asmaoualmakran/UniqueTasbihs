from django.db import models
import datetime
from UnTasApp.models.customer import Customer
from UnTasApp.models.item import Item
from UnTasApp.models.address import Address

#Primary key fields are set on null=True for debuggin purpuses

class Order(models.Model):
	customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True)
	item_id 	= models.ForeignKey(Item, on_delete=models.PROTECT, null=True)
	delivery_id = models.ForeignKey(Address, related_name='%(class)s_delivery', on_delete=models.PROTECT, null=True)
	billing_id = models.ForeignKey(Address, related_name='%(class)s_billing',on_delete=models.PROTECT, null=True)
	TAV			= models.IntegerField(null=False)
	discount	= models.IntegerField()
	price_total = models.IntegerField(null=False)
	
#	date = models.DateField((auto_now_add=True, editable=False)