from django.db import models
import datetime
from order import Order 


class Sales(models.Model):
	order_id = models.ForeignKey(Order, on_delete=PROTECT, null=False)
	date = models.DateField((auto_now_add=True, editable=False)