from rest_framework import serializers
from UnTasApp.models.item import Item as itemModel


class Item(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)
	discount_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
	category_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	
	class Meta:
		model = itemModel
		fields = ('id','category_id','discount_id','barcode','name','selling_price','buying_price','color','image','state')
		extra_kwargs = {'category_id':{'view_name': 'api:category-detail'},'discount_id':{'view_name':'api:discount-detail'}}


class CreateItem(serializers.HyperlinkedModelSerializer):
	# for the choice field, ChoiceField supported by REST
#	state = serializers.CharField(source='get_state_display')

	#to enable the choices
#	def get_state(self,obj):
#		return obj.get_state_display()

	class Meta:
		model = itemModel
		fields = ('category_id','discount_id','barcode','name','selling_price','buying_price','color','image','state')


