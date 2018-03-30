from rest_framework import serializers 
from UnTasApp.models.sales import Sales as salesModel


class Sales(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)
	order = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = salesModel
		fields = ('id','order','date')
		extra_kwargs = {'order':{'view_name':'api:order-detail'}}


class CreateSales(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = salesModel
		fields = ('order','date')