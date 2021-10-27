from rest_framework import status
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from offers.models import Offers
from offers.Api.serializers import offersSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class OfferApiList(APIView):
   
    permission_classes = [IsAuthenticated]
    def get(self,reqest):
        
        try:
            offer = Offers.objects.all()
            serializer = offersSerializer(offer, many = True)
            return Response(serializer.data)
        except Offers.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    



class PostOffer(APIView):
  
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = offersSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class UpdatOffer(APIView):
 
    permission_classes = [IsAuthenticated]


    def get_object(self,id):

        try:
            return Offers.objects.get(id=id)
        except Offers.DoesNotExist:
            return Http404 

    
    def get(self , request, id):
        product = self.get_object(id)
        serializer = offersSerializer(product, context={"request": request})
        return Response(serializer.data)        

    def put(self,request,id):
        
        product = self.get_object(id)
        serializer = offersSerializer(product ,data=request.data, context={"request": request}) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data )  
        return Response(serializer.errors ,status= status.HTTP_400_BAD_REQUEST)         


     
    def delete(self,request ,id):
        offer= self.get_object(id)
        if offer == Http404:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            offer.is_archived = True
            offer.save()
            return Response(status= status.HTTP_200_OK)              