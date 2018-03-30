from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from UnTasApp.serializers.order import Order as orderSerializer
from UnTasApp.serializers.order import CreateOrder as createOrderSerializer
from UnTasApp.models.order import Order as orderModel


@api_view(['GET','POST'])
def orderRequest(request):
	if(request.method == 'GET'):
		orders = orderModel.objects.all()
		serializer = orderSerializer(orders, many=True, context={'request':request})
		return Response(serializer.data)
	elif(request.method == 'POST'):
		serializer = createOrderSerializer(data=request.data)
		if(serializer.is_valid()):
			order = serializer.save()
			serializer = orderSerializer(order, context={'request':request})
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	

@api_view(['GET','PUT','DELETE'])
def singleOrderRequest(request,pk):
	try:
		order = orderModel.objects.get(id=pk)
	except orderModel.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if(request.method == 'GET'):
		serializer = orderSerializer(order, context={'request':request})
		return Response(serializer.data, status=status.HTTP_200_OK)

	elif(request.method == 'PUT'):
		serializer = orderSerializer(order, data=request.data, context={'request':request})

		if(serializer.is_valid()):
			serializer.save()
			return Response(status=status.HTTP_204_NO_CONTENT)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	else:
		order.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)