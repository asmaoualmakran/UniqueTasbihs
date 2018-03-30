from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from UnTasApp.serializers.item import Item as itemSerializer
from UnTasApp.serializers.item import CreateItem as createItemSerializer
from UnTasApp.models.item import Item as itemModel

@api_view(['GET','POST'])
def itemRequest(request):
	if(request.method == 'GET'):
		items = itemModel.objects.all()
		serializer = itemSerializer(items, many=True, context={'request':request})
		return Response(serializer.data)
	elif(request.method == 'POST'):
		serializer = createItemSerializer(data=request.data)
		if(serializer.is_valid()):
			item = serializer.save()
			serializer = itemSerializer(item, context={'request':request})
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def singleItemRequest(request,pk):
	try:
		item = itemModel.objects.get(id=pk)
	except itemModel.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if(request.method == 'GET'):
		serializer = itemSerializer(item, context={'request':request})
		return Response(serializer.data, status=status.HTTP_200_OK)

	elif(request.method == 'PUT'):
		serializer = itemSerializer(item, data=request.data, context={'request':request})

		if(serializer.is_valid()):
			serializer.save()
			return Response(status=status.HTTP_204_NO_CONTENT)
		return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
	else:
		item.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)