from django.db import models
import datetime
from UnTasApp.models.customer import Customer
from UnTasApp.models.item import Item
from UnTasApp.models.address import Address
from UnTasApp.models.discount import Discount

#Primary key fields are set on null=True for debuggin purpuses

class Order(models.Model):

	IN_PROGRESS = 'IP'
	ENQUED = 'ENQ'
	AWAITING_PAYEMENT = 'AP'
	AWAITING_DELIVERY = 'AD'
	COMPLETED = 'COM'
	CANCELED = 'CA'

	ORDER_STATUS_CHOICES = (
		(IN_PROGRESS, 'in progress'),
		(ENQUED, 'enqued'),
		(AWAITING_PAYEMENT, 'awaiting payement'),
		(AWAITING_DELIVERY, 'awaiting delivery'),
		(COMPLETED, 'completed'),
		(CANCELED, 'canceled'),
		)

	customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT, null=False)
	item_id 	= models.ForeignKey(Item, on_delete=models.PROTECT, null=False)
	delivery_id = models.ForeignKey(Address, related_name='%(class)s_delivery', on_delete=models.PROTECT, null=False)
	billing_id = models.ForeignKey(Address, related_name='%(class)s_billing',on_delete=models.PROTECT, null=False)
	discount_id	= models.ForeignKey(Discount, on_delete=models.PROTECT, null=False)
	TAV			= models.IntegerField(null=False)
	price_total = models.IntegerField(null=False)
	date = models.DateField(auto_now=True, editable=False)
	status = models.CharField(max_length=100, choices=ORDER_STATUS_CHOICES, default=IN_PROGRESS)