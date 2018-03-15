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