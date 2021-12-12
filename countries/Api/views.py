from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from countries.models import Countries
from cities.models import Cities
from area.models import Area
from area.Api.serializers import AreaSerializer
# from countries.Api.serializers import CountriesSerailizer
from cities.Api.serializers import CitiesSerailizer

# class CountriesApiList(APIView):
#     def get(self,requset):
        
#        try:
#            countries =Countries.objects.all()
#            country_serializer = CountriesSerailizer(countries, many=True)
#            for country in country_serializer.data:
#                cities = Cities.objects.filter(country_name=country['id'])
#                cities_serializer = CitiesSerailizer(cities,many=True)
#                country['cities'] = cities_serializer.data
#                for city in cities_serializer.data:
#                    areas = Area.objects.filter(city_name=city['id'])
#                    area_serializer = AreaSerializer(areas,many= True)
#                    city['areas'] = area_serializer.data
#            return Response(country_serializer.data ,status=status.HTTP_200_OK)
#        except Exception as e :
#             return Response({'error':'some thing went wrong'},status= status.HTTP_400_BAD_REQUEST)

