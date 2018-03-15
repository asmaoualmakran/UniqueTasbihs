from rest_framework import serializers
from UnTasApp.models.order import Order as orderModel


class Order(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)
	customer_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
	item_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	delivery_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
	billing_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
	discount_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = orderModel
		fields = ('id','customer_id','item_id','delivery_id','billing_id','discount_id','TAV','price_total','date', 'status')
		extra_kwargs = {'customer_id':{'view_name':'api:customer-detail'},'item_id':{'view_name':'api:item-detail'},'delivery_id':{'view_name':'api:address-detail'},'billing_id':{'view_name':'api:address-detail'},'discount_id':{'view_name':'api:discount-detail'}}

class CreateOrder(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = orderModel
		fields = ('customer_id','item_id','delivery_id','billing_id','discount_id','TAV','price_total','date', 'status')
		