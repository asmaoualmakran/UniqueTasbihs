from rest_framework import serializers 
from UnTasApp.models.sales import Sales as salesModel


class Sales(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)
	order_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = salesModel
		fields = ('id','order_id','date')
		extra_kwargs = {'order_id':{'view_name':'api:order-detail'}}


class CreateSales(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = salesModel
		fields = ('order_id','date')