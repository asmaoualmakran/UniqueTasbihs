from rest_framework import serializers
from UnTasApp.models.itemCategory import ItemCategory as itemCategoryModel


class ItemCategoty(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	item_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = itemCategoryModel
		fields = ('id','item_id')
		extra_kwargs = {'item_id':{'view_name':'api:item-detail'}}


class CreateItemCategory(serializers.ModelSerializer):
	model = itemCategoryModel
	fields = ('item_id')