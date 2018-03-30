from rest_framework import serializers
from UnTasApp.models.order import Order as orderModel


class Order(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)
	customer = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
	item = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	delivery = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
	billing = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
	discount = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = orderModel
		fields = ('id','customer','item','delivery','billing','discount','TAV','price_total','date', 'status')
		extra_kwargs = {'customer':{'view_name':'api:customer-detail'},'item':{'view_name':'api:item-detail'},'delivery_id':{'view_name':'api:address-detail'},'billing_id':{'view_name':'api:address-detail'},'discount_id':{'view_name':'api:discount-detail'}}

class CreateOrder(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = orderModel
		fields = ('customer','item','delivery','billing','discount_id','TAV','price_total','date', 'status')
		