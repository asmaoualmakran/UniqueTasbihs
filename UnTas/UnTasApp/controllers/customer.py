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