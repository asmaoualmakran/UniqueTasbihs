from django.db import models
from UnTasApp.models.userBase import UserBase
# from order import Order

class Customer(UserBase):
	pass
	# user = models.OneToOneField(UserBase, related_name='customers')
	 order_id = models.ForeignKey(on_delete=PROTECT,null=True)
	 address_id = models.ForeignKey(on_delete=PROTECT)