from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from UnTasApp.serializers.customer import Customer as customerSerializer
from UnTasApp.serializers.customer import CreateCustomer as CreateCustomerSerializer
from UnTasApp.models.customer import Customer as customerModel


@api_view(['GET','POST'])
def customerRequest(request):
	if(request.method == 'GET'):
		customers = customerModel.objects.all()
		serializer = customerSerializer(customers, many=True, context={'request':request})
		return Response(serializer.data)
	elif(request.method == 'POST'):
		serializer = CreateCustomerSerializer(data=request.data)
		if(serializer.is_valid()):
			customer = serializer.save()
			serializer = customerSerializer(customer, context={'request':request})
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def singleCustomerRequest(request,pk):
	try: 
		customer = customerModel.objects.get(id=pk)
	except customerModel.DoesNotExist: 
		return Response(status=status.HTTP_404_NOT_FOUND)

	if(request.method == 'GET'):
		serializer = customerSerializer(customer, context={'request':request})
		return Response(serializer.data, status=status.HTTP_200_OK)
	
	elif(request.method == 'PUT'):
		serializer = customerSerializer(customer, data=request.data, context={'request':request})

		if(serializer.is_valid()):
			serializer.save()
			return Response(status=status.HTTP_204_NO_CONTENT)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	else:
		customer.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)