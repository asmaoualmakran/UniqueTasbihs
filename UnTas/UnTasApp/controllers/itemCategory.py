from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from UnTasApp.serializers.itemCategory import ItemCategory as categorySerializer
from UnTasApp.serializers.itemCategory import CreateItemCategory as createCategorySerializer
from UnTasApp.models.itemCategory import ItemCategory as categoryModel

@api_view(['GET','POST'])
def itemCategoryRequest(request):
	if(request.method == 'GET'):
		categories = categoryModel.objects.all()
		serializer = categorySerializer(categories, many=True, context={'request':request})
		return Response(serializer.data)
	elif(request.method == 'POST'):
		serializer = categorySerializer(data=request.data)
		if(serializer.is_valid()):
			serializer = categorySerializer(serializer.save(), context={'request':request})
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
