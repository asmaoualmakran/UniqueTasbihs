from rest_framework import serializers
from UnTasApp.models.item import Stock as stockModel


class Stock(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	item_id = serializers.PrimaryRelatedField(many=False, read_only=True)

	class Meta:
		model = stockModel
		fields = ('id','item_id','amount')
		extra_kwargs = {'item_id':{'view_name':'api:item-detail'}}


class CreateStock(serializers.ModelSerializer):

	class Meta:
		model = stockModel
		fields = ('item_id','amount')