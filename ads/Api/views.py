from rest_framework import serializers, status ,generics 
from django.http import Http404 
from rest_framework.response import Response
from ads.models import Ads
from rest_framework.views import APIView
from ads.Api.serializers import AdsSerializer
from rest_framework.permissions import IsAuthenticated




class AdsList(generics.ListAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = AdsSerializer

    def get(self,request):
        try:
           ads = Ads.objects.all()
           serializer =AdsSerializer(ads,many = True)
           return Response(serializer.data)
        except Ads.DoesNotExist:
            return Http404    
                 


class AdsAdd(APIView):
    
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = AdsSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)