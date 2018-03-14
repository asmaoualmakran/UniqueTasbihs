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
		serializer = itemSerializer(data=request.data)
		if(serializer.is_valid()):
			serializer.save()
			it = serializer.save()
			serializer = itemSerializer(it, context={'request':request})
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)