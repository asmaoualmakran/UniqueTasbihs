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
		serializer = createDiscountSerializer(data=request.data)
		if(serializer.is_valid()):
			discount = serializer.save()
			serializer = discountSerializer(discount, context={'request':request})
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def singleDiscountRequest(request,pk):
	try:
		discount = discountModel.objects.get(id=pk)
	except discountModel.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if(request.method == 'GET'):
		serializer = discountSerializer(discount, context={'request':request})
		return Response(serializer.data, status=status.HTTP_200_OK)
	
	elif(request.method == 'PUT'):
		serializer = discountSerializer(discount, data=request.data, context={'request':request})	

		if(serializer.is_valid()):
			serializer.save()
			return Response(status=status.HTTP_204_NO_CONTENT)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	else: 
		discount.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)	