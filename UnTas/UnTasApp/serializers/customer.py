from rest_framework import serializers
from UnTasApp.models.customer import Customer as customerModel


class Customer(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)
	address = serializers.HyperlinkedIdentityField(view_name = 'api:address-detail')

	class Meta: 
		model = customerModel
		fields = ('id','address','first_name','last_name','birthday','email')
		extra_kwargs = {'address':{'view_name': 'api:address-detail'},}

class CreateCustomer(serializers.HyperlinkedModelSerializer):
	
	class Meta: 
		model = customerModel
		fields = ('address','first_name','last_name','birthday','email')
