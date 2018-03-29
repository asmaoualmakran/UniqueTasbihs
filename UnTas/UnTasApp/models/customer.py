from django.db import models, IntegrityError
from UnTasApp.models.userBase import UserBase
from UnTasApp.models.address import Address
# from order import Order

class Customer(UserBase):
	# user = models.OneToOneField(UserBase, related_name='customers')
	# order_id = models.ForeignKey(on_delete=PROTECT,null=True)
	 address_id = models.ForeignKey(Address, on_delete=models.PROTECT)
	# first_name = models.CharField(max_length=100)
	# last_name = models.CharField(max_length=100)
	# birthday = models.CharField(max_length=100)
	# email = models.CharField(max_length=100)