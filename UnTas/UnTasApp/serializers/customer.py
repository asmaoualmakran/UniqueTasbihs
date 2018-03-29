from rest_framework import serializers
from UnTasApp.models.customer import Customer as customerModel


class Customer(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)
	address_id = serializers.HyperlinkedIdentityField(view_name = 'address-detail')

	class Meta: 
		model = customerModel
		fields = ('id','address_id','first_name','last_name','birthday','email')
		extra_kwargs = {'address_id':{'view_name': 'api:address-detail'},}

class CreateCustomer(serializers.HyperlinkedModelSerializer):

	class Meta: 
		model = customerModel
		fields = ('address_id','first_name','last_name','birthday','email')