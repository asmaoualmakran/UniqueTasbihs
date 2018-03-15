from rest_framework import serializers
from UnTasApp.models.discount import Discount as discountModel


class Discount(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta:
		model = discountModel
		fields=('id','percentage')


class CreateDiscount(serializers.ModelSerializer):

	class Meta:
		model = discountModel
		fields = ('percentage',)