from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'address': reverse('api:address', request=request, format=format),
        'discount': reverse('api:discount', request=request, format=format),
    	'item': reverse('api:item', request=request, format=format),
 		'category': reverse('api:category', request=request, format=format),
    	'order': reverse('api:order', request=request, format=format),
    })