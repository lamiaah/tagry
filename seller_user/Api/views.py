from rest_framework.views import APIView
from users.Api.api_register import register
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated
from products.models import Products 
from seller_user.models import Seller
from seller_user.Api.serializers import SellerSerializer
from products.Api.serializers import ImageSerializers, ProductSerializer 

from seller_user.Api.api_register_seller import register_seller_user


class RegisterSeller(APIView):

   
    def post(self, request):

        try:
            custom_user_data = {
                'email' : request.data.get('email'),
                'password' : request.data.get('password'),
                'username' : request.data.get('username'),
            }
           
            custom_user_register = register(custom_user_data)
            print(custom_user_register)
            if custom_user_register['error_code'] == 2:
                return Response(custom_user_register['serializer_msg'], status = status.HTTP_400_BAD_REQUEST)
            elif custom_user_register['error_code'] == 4:
                return Response(custom_user_register['serializer_msg'], status = status.HTTP_400_BAD_REQUEST)
            elif custom_user_register['error_code'] == 1 or custom_user_register['error_code'] == 3:
                couser_data = {
                    'user' : custom_user_register['serializer_msg'],
                    'name' : request.data.get('name'),
                    'website' : request.data.get('website'),
                    'about' : request.data.get('about'),
                    'seller_address' : request.data.get('seller_address'),
                    'city_name' : request.data.get('city_name'),
                    'country_name' : request.data.get('country_name'),
                    'image' : request.data.get('image'),
                    'category_id': request.data.get('category_id'),
                    'area_name' : request.data.get('area_name'),
                  }

                seller_user_register = register_seller_user(couser_data)
               
                if seller_user_register['error_code'] == 2:
                    return Response(seller_user_register['serializer_msg'], status = status.HTTP_400_BAD_REQUEST)
                elif seller_user_register['error_code'] == 4:
                    return Response(seller_user_register['serializer_msg'], status = status.HTTP_400_BAD_REQUEST)
                elif seller_user_register['error_code'] == 1:
                    return Response(seller_user_register['serializer_msg'], status = status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(seller_user_register['serializer_msg'], status = status.HTTP_201_CREATED)



        except Exception as e:
            return Response(str(e), status = status.HTTP_400_BAD_REQUEST)



    

 
class Get_Product(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    def get(self,pk):
        try:
            product = Products.objects.filter(is_archived=False,seller_id = pk)
            return Response(product)
        except Products.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



                 
class Get_Seller(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,requset):
        try:
            seller = Seller.objects.all()
            serializer = SellerSerializer(seller, many = True)
            return Response(serializer.data)
        except Seller.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


