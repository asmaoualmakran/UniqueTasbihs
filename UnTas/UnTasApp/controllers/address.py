from rest_framework import status
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from UnTasApp.serializers.address import Address as addressSerializer
from UnTasApp.serializers.address import CreateAddress as createAddressSerializer
from UnTasApp.models.address import Address as addressModel


@api_view(['GET','POST'])
def addressRequest(request):
	if(request.method == 'GET'):
		addresses = addressModel.objects.all()
		serializer = addressSerializer(addresses, many=True, context={'request':request})
		return Response(serializer.data)
	elif(request.method == 'POST'):
		serializer = createAddressSerializer(data=request.data)
		if(serializer.is_valid()):
			address = serializer.save()
			serializer = addressSerializer(address, context={'request':request})
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def singleAddressRequest(request, pk):
	try: 
		address = addressModel.objects.get(id=pk)
	except addressModel.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if(request.method == 'GET'):
		serializer = addressSerializer(address, context={'request':request})
		return Response(serializer.data, status=status.HTTP_200_OK)
	elif(request.method == 'PUT'):
		serializer = addressSerializer(address, data=request.data, context={'request':request})	

		if(serializer.is_valid()):
			serializer.save()
			return Response(status=status.HTTP_204_NO_CONTENT)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	else:
		address.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)		