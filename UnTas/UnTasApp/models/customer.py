from django.db import models
from django.contrib.auth.models import User
from oder import Order

class Customer(User):
	order_id = models.ForeignKey(on_delete=PROTECT,null=True)