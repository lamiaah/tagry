from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from countries.models import Countries
from countries.Api.serailizers import CountriesSerailizer

class CountriesApiList(APIView):
    def get(self,requset):
        
        try:
            country = Countries.objects.all()
            serializer = CountriesSerailizer(country, many = True)
            return Response(serializer.data)
        except Cities.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    
