from rest_framework import serializers
from UnTasApp.models.itemCategory import ItemCategory as itemCategoryModel


class ItemCategory(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	
	class Meta:
		model = itemCategoryModel
		fields = ('id', 'categoryName')
#		extra_kwargs = {'item_id':{'view_name':'api:item-detail'}}


class CreateItemCategory(serializers.ModelSerializer):
	model = itemCategoryModel
	fields = ('categoryName')