from rest_framework import serializers
from UnTasApp.models.itemCategory import ItemCategory as itemCategoryModel


class ItemCategory(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	
	class Meta:
		model = itemCategoryModel
		fields = ('id', 'categoryName')


class CreateItemCategory(serializers.ModelSerializer):

	class Meta:
		model = itemCategoryModel
		fields = ('categoryName',)