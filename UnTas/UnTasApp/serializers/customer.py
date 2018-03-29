from rest_framework import serializers
from UnTasApp.models.customer import Customer as customerModel


class Customer(serializers.HyperlinkedModelSerializer):
	customer_address = serializers.HyperlinkedIdentityField(view_name = 'address-detail')

	class Meta: 
		model = customerModel
		fields = ('id','customer_address','first_name','last_name','birthday','email')


class CreateCustomer(serializers.HyperlinkedModelSerializer):

	class Meta: 
		model = customerModel
		fields = ('customer_address','first_name','last_name','birthday','email')