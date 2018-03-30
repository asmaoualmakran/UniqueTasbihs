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
		serializer = createCategorySerializer(data=request.data)
		if(serializer.is_valid()):
			itemCategory = serializer.save()
			serializer = categorySerializer(itemCategory, context={'request':request})
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def singleItemCategoryRequest(request,pk):
	try:
		category = categoryModel.objects.get(id=pk)
	except categoryModel.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if(request.method == 'GET'):
		serializer = categorySerializer(category, context={'request':request})
		return Response(serializer.data, status=status.HTTP_200_OK)

	elif(request.method == 'PUT'):
		serializer = categorySerializer(category, data=request.data, context={'request':request})

		if(serializer.is_valid()):
			serializer.save()
			return Response(status=status.HTTP_204_NO_CONTENT)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	else:
		category.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)