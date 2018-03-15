from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from UnTasApp.serializers.sales import Sales as salesSerializer
from UnTasApp.serializers.sales import CreateSales as createSalesSerializer
from UnTasApp.models.sales import Sales as salesModel


@api_view(['GET','POST'])
def salesRequest(request):
	if(request.method == 'GET'):
		sales = salesModel.objects.all()
		serializer = salesSerializer(sales, many=True, context={'request':request})
		return Response(serializer.data)
	elif(request.method == 'POST'):
		serializer = createSalesSerializer(data=request.data)
		if(serializer.is_valid()):
			sales = serializer.save()
			serializer =salesSerializer(sales, context={'request':request})
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)