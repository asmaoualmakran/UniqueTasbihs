from rest_framework import serializers
from UnTasApp.models.stock import Stock as stockModel


class Stock(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)
	item_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

	class Meta:
		model = stockModel
		fields = ('id','item_id','amount')
		extra_kwargs = {'item_id':{'view_name':'api:item-detail'}}


class CreateStock(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = stockModel
		fields = ('item_id','amount')