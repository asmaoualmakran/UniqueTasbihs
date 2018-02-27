from rest_framewrok import serializers
from UnTasApp.models.address import Address as addressModel


class Address(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta:
		model = addressModel
		fields = ('id','street','number','zip_code','city','country')


class CreateAddress(serializers.ModelSerializer):

	class Meta:
		model = addressModel
		fields = ('street','number','zip_code','city','country')