from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from UnTasApp.serializers.stock import Stock as stockSerializer
from UnTasApp.serializers.stock import CreateStock as createStockSerializer
from UnTasApp.models.stock import Stock as stockModel


@api_view(['GET','POST'])
def stockRequest(request):
	if(request.method == 'GET'):
		stocks = stockModel.objects.all()
		serializer = stockSerializer(stocks, many=True, context={'request':request})
		return Response(serializer.data)
	elif(request.method == 'POST'):
		serializer = createStockSerializer(data=request.data)
		if(serializer.is_valid()):
			stock = serializer.save()
			serializer = stockSerializer(stock, context={'request':request})
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def singleStockRequest(request, pk):
	try:
		stock = stockModel.objects.get(id=pk)
	except stockModel.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if(request.method == 'GET'):
		serializer = stockSerializer(stock, context={'request':request})
		return Response(serializer.data, status=status.HTTP_200_OK)

	elif(request.method == 'PUT'):
		serializer = stockSerializer(stock, data=request.data, context={'request':request})

		if(serializer.is_valid()):
			serializer.save()
			return Response(status=status.HTTP_204_NO_CONTENT)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	else:
		stock.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)