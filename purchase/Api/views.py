from django.http.response import Http404
from rest_framework import status ,generics 
from purchase.models import Purchase
from purchase.Api.serializers import PurchaseSerailizer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class PurchaseApi(generics.ListAPIView):
  
    permission_classes = [IsAuthenticated]
    serializer_class = PurchaseSerailizer

    def get_queryset(self):
        shopping_cart = self.kwargs.get('shopping_cart')
        
        try:
            return Purchase.objects.filter(shopping_cart_id=shopping_cart , is_archive = True)
        except Purchase.DoesNotExist:
            return Http404
    
class AddPurchase(APIView):
   
    permission_classes = [IsAuthenticated]


    def post(self, request):
        serializer = PurchaseSerailizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

class DeleteProduct(APIView):
    
    permission_classes = [IsAuthenticated]
    

    
    def get_object(self,id):

        try:
            return Purchase.objects.get(id=id)
        except Purchase.DoesNotExist:
            return Http404 

    
    def get(self , request, id):
        purchase = self.get_object(id)
        serializer = PurchaseSerailizer(purchase, context={"request": request})
        return Response(serializer.data)        


    def delete(self,request ,id):
        purchase= self.get_object(id)
        if purchase == Http404:
            return Response( status = status.HTTP_400_BAD_REQUEST)
        else:    
            purchase.is_archived = True
            purchase.save()
            return Response(status= status.HTTP_204_NO_CONTENT)                 

       