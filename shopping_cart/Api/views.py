
from django.http.response import Http404
from rest_framework import status ,generics 
from rest_framework.views import APIView
from rest_framework.response import Response
from shopping_cart.models import Shopping_cart ,Shopping_cart_product
from shopping_cart.Api.serializers import ShoppingCartSerializer , ShoppingProductSerializer
from products.models import Products
from offers.models import Offers
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

def total(shopping_products):
    for shopping_product in shopping_products:
       sha = shopping_product

       print(sha)
    return 

         
def shoppingcart_product(shopping_cart):

    for shopping in shopping_cart :  
        shopping_product = Shopping_cart_product.objects.filter (shopping_cart_product_id=shopping['id']) 
        sh = total(shopping_product)
       
        shopping_product_serialzers = ShoppingProductSerializer(data =shopping_product, many =True)

        shopping_product_serialzers.is_valid()
       # print(shopping_product_serialzers)
        shopping['shopping_product'] = shopping_product_serialzers.data
       
    
    return shopping_cart
 

class ShoppingApi(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ShoppingCartSerializer
    
    def get(self,request ,user_id ):
        try:
           # user_id = self.kwargs.get('user_id')
            shopping  = Shopping_cart.objects.filter(user_id = user_id , is_archived = False)
            shooping_product = ShoppingCartSerializer(shopping ,many=True)
            serializer_shopping = shoppingcart_product(shooping_product.data)
           # print(serializer_shopping)
            return Response(serializer_shopping)
        except Shopping_cart.DoesNotExist:
            return Response(status = status.HTTP_400_BAD_REQUEST) 
    

class AddShopping(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ShoppingCartSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            shopping_product_data ={
                'shopping_cart_product': str(serializer.data['id']),
                'product_id': request.data['product_id']
            }
            shoppingproduct_serializer = ShoppingProductSerializer(data= shopping_product_data)

            if shoppingproduct_serializer.is_valid():
                shoppingproduct_serializer.save()
                return Response(shoppingproduct_serializer.data, status= status.HTTP_201_CREATED)  
            else:
                return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        else:    
           return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    # def cal_total_price( self,serializer , offer_id):
    #     offer = Offers.objects.get(id=offer_id)
    #     offer = serializer.validated_data.get('discount')

    #     product_id = serializer.validated_data.get('products_id')
    #     product = Products.objects.get(id = product_id.id)
    
    #     total_price = (product.product_price * serializer.validated_data.get('discount')) * serializer.validated_data.get('quantity')
    #     return total_price
        

class ShoppingPut(APIView):

    def get_object(self,id):

        try:
            return Shopping_cart.objects.get(id=id)
        except Shopping_cart.DoesNotExist:
            return Http404 

    
    def get(self , request, id):
        product = self.get_object(id)
        serializer = ShoppingCartSerializer(product, context={"request": request})
        shopping_product = shoppingcart_product(serializer.data)
        return Response(shopping_product)        

    def put(self,request,id):
        
        product = self.get_object(id)
        serializer = ShoppingCartSerializer(product ,data=request.data, context={"request": request}) 
        if serializer.is_valid():
            serializer.save()
            shopping_product ={
             'shopping_cart_product': str(serializer.data['id']),
             'product_id': request.data['product_id']
            }
            print(shopping_product)
            shopping_product_serializer = ShoppingProductSerializer(data= shopping_product)
            if shopping_product_serializer.is_valid():
                shopping_product_serializer.save()
                return Response(shopping_product_serializer.data, status= status.HTTP_201_CREATED)  
            else:
                return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST) 
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST) 
    
          
        
    def delete(self,request ,id):
        shopping= self.get_object(id)
        if shopping == Http404:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            shopping.is_archived = True
            shopping.save()
            return Response(status= status.HTTP_200_OK)  
    


