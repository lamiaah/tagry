from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from cities.models import Cities
from cities.Api.serializers import CitiesSerailizer

class CitiesApiList(APIView):
    def get(self,requset):
        
        try:
            city = Cities.objects.all()
            serializer = CitiesSerailizer(city, many = True)
            return Response(serializer.data)
        except Cities.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    
