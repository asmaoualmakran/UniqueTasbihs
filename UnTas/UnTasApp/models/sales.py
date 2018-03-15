from django.db import models
import datetime
from UnTasApp.models.order import Order 

class Sales(models.Model):
	order_id = models.OneToOneField(Order, on_delete=models.PROTECT, null=False)
	date = models.DateField(auto_now=True, editable=False)