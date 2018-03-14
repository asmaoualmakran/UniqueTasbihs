from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from UnTasApp.serializers.discount import Discount as discountSerializer
from UnTasApp.serializers.discount import CreateDiscount as createDiscountSerializer
from UnTasApp.models.discount import Discount as discountModel

@api_view(['GET','POST'])
def discountRequest(request):
	if(request.method == 'GET'):
		discounts = discountModel.objects.all()
		serializer = discountSerializer(discounts, many=True, context={'request':request})
		return Response(serializer.data)
	elif(request.method == 'POST'):
		serializer = discountSerializer(data=request.data)
		if(serializer.is_valid()):
			serializer.save()
			serializer = discountSerializer(serializer.save(), context={'request':request})
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)