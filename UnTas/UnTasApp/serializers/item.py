from rest_framework import serializers
from UnTasApp.models.item import Item as itemModel

#TODO: replace the PrimaryKeyRelatedField with, HyperlinkedIdentityField

class Item(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)
	discount = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
	category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	
	class Meta:
		model = itemModel
		fields = ('id','category','discount','barcode','name','selling_price','buying_price','color','image','state')
		extra_kwargs = {'category':{'view_name': 'api:category-detail'},'discount':{'view_name':'api:discount-detail'}}


class CreateItem(serializers.HyperlinkedModelSerializer):
	# for the choice field, ChoiceField supported by REST
#	state = serializers.CharField(source='get_state_display')

	#to enable the choices
#	def get_state(self,obj):
#		return obj.get_state_display()

	class Meta:
		model = itemModel
		fields = ('category','discount','barcode','name','selling_price','buying_price','color','image','state')


