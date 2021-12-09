from rest_framework import serializers, status ,generics 
from django.http import Http404 
from rest_framework.response import Response
from stores.models import SellerStores
from rest_framework.views import APIView
from stores.Api.serializers import SellerStoresSerializer
from rest_framework.permissions import IsAuthenticated




class SellerStoresList(generics.ListAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = SellerStoresSerializer

    def get(self,request):
        try:
           stores = SellerStores.objects.all()
           serializer =SellerStoresSerializer(SellerStores,many = True)
           return Response(serializer.data)
        except SellerStores.DoesNotExist:
            return Http404    
                 


class SellerStoresAdd(APIView):
    
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = SellerStoresSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PutSellerStores(APIView):
    
    permission_classes = [IsAuthenticated]
    def get_object(self, id):
        try:
            return SellerStores.objects.get(id=id)
        except SellerStores.DoesNotExist:
            return Http404


    def get(self,request ,id):

        stores = self.get_object(id)
        serializer = SellerStoresSerializer(stores , context = {"request":request}) 
        return Response(serializer.data)


    def put(self ,request ,id ):
        stores = self.get_object(id)
        serializer = SellerStoresSerializer(stores ,data=request.data , context = {"request":request}) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors ,status= status.HTTP_400_BAD_REQUEST)

    def delete(self,request ,id):
        stores= self.get_object(id)
        if stores == Http404:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            stores.is_archived = True
            stores.save()
            return Response(status= status.HTTP_200_OK) 
