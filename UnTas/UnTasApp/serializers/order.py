from rest_framework import serializers
from UnTasApp.models.order import Order as orderModel


class Order(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	item_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = orderModel
		fields = ('id','customer_id','item_id','TAV','discount','price_total','delivery_address','billing_address','date')
		extra_kwargs = {'customer_id':{'view_name': 'api:customer-detail'},'item_id':{'view_name:item-detail'},'delivery_address':{'view_name:address-detail'},'billing_address':{'view_name:address-detail'}}

class CreateOrder(serializers.ModelSerializer):

	class Meta:
		model = orderModel
		fields = ('customer_id','item_id','TAV','discount','price_total','delivery_address','billing_address','date')