
from buyer.Api.serializer import  BuyerSerializer
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.views import APIView
from django.contrib.auth import authenticate, logout, login
from users.models import CustomUser
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from users.Api.serializers import RegistrationSerializer

from buyer.models import Buyer
from users.Api.api_register import register, validate_token
from buyer.Api.api_register_buyer import register_buyer
from users.Api.views import login_user



class LoginBuyer(APIView):

    def post(self, request):

        try:
            res = login_user(request)

            if res['status_code'] == '200':
                user_id = CustomUser.objects.get(email = request.data.get('email'))
                user = Buyer.objects.get(user_id = user_id.id)
                res['user_data'] = {
                    'id' : user_id.id,
                    'email' : user_id.email,
                    'username' : user_id.username,
                    # 'user_address' : '{}, {}, {}'.format(user.area.country.country_name, user.area.city.city_name, user.area.area_name),
                    'name' : user.name,
                    'about' : user.about,
                    'image' : user.image,
                    'city' :user.city,
                    'country':user.country,
                    'area':user.area,
                    'address':user.address,
                    
                }
                return Response(res, status = status.HTTP_200_OK)
            elif res['status_code'] == '401':
                return Response(res, status = status.HTTP_401_UNAUTHORIZED)
            else:
                return Response(res, status = status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status = status.HTTP_404_NOT_FOUND)




class RegisterBuyer(APIView):


    def post(self, request):

        try:
            custom_user_data = {
                'email' : request.data.get('email'),
                'password' : request.data.get('password'),
                'username' : request.data.get('username'),
            }

            custom_user_register = register(custom_user_data)

            if custom_user_register['error_code'] == 2:
                return Response(custom_user_register['serializer_msg'], status = status.HTTP_400_BAD_REQUEST)
            elif custom_user_register['error_code'] == 4:
                return Response(custom_user_register['serializer_msg'], status = status.HTTP_400_BAD_REQUEST)
            elif custom_user_register['error_code'] == 1 or custom_user_register['error_code'] == 3:
                end_user_data = {
                    'user_id' : custom_user_register['serializer_msg']['user_id'],
                    'area' : request.data.get('area'),
                    'address' : request.data.get('address'),
                    'name' : request.data.get('name'),
                    'about' : request.data.get('about'),
                    'city' : request.data.get('city'),
                    'country' : request.data.get('country'),
                    'image' : request.data.get('image'),
                }

                end_user_register = register_buyer(end_user_data)

                if end_user_register['error_code'] == 2:
                    return Response(end_user_register['serializer_msg'], status = status.HTTP_400_BAD_REQUEST)
                elif end_user_register['error_code'] == 4:
                    return Response(end_user_register['serializer_msg'], status = status.HTTP_400_BAD_REQUEST)
                elif end_user_register['error_code'] == 1:
                    return Response(end_user_register['serializer_msg'], status = status.HTTP_400_BAD_REQUEST)
                else:
                    end_user_register['serializer_msg']['user_name'] = custom_user_register['serializer_msg']['user_name']
                    return Response(end_user_register['serializer_msg'], status = status.HTTP_201_CREATED)

        except Exception as e:
            return Response(str(e), status = status.HTTP_400_BAD_REQUEST)





class GetBuyerData(APIView):


    permission_classes = [IsAuthenticated]


    def get(self, request, user_id):

        try:
            token_validator = validate_token(request, user_id)

            if token_validator == True:
                user_data = {}
                custom_user = CustomUser.objects.get(pk = user_id)
                user_data['id'] = custom_user.id
                user_data['email'] = custom_user.email
                user_data['username'] = custom_user.username
                end_user = Buyer.objects.get(user_id = custom_user.id)
                # user_data['user_address'] = f'{end_user.area.country.country_name}, {end_user.area.city.city_name}, {end_user.area.area_name}'
                user_data['about'] = end_user.about
                user_data['name'] = end_user.name
                user_data['image'] = end_user.image
                user_data['country'] = end_user.country
                return Response(user_data, status = status.HTTP_200_OK)
            
            else:
                return Response({'error' : 'invalid user data'}, status = status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            print(e)
            return Response({'error' : 'some thing went wrong'}, status = status.HTTP_400_BAD_REQUEST)

# class BuyerLogin(APIView):

#     def post(self, request):
    
#         email = request.data.get('email')
#         password = request.data.get('password')
#         validate = authenticate(email= email, password = password)

#         if validate:
#             login(request, validate)
#             us = CustomUser.objects.get(email = email)
#             datax =  {'id': us.id,
#                     'token' : validate.auth_token.key,
#                     'email' : request.data['email']
#                 }
#             x=  datax['id']
#             if request.method == 'POST':
              
#                 serializer =BuyerSerializer(data = request.data ,many= True)
#                 request.data["user_id"] = x
#                 if serializer.is_valid():      
#                     serializer.save()  
#                     return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)      
#                 else:
                
#                     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 
        
# class BuyerInfo(APIView):
  
  
#     def post(self, request ,user_id):
#         try:
#             user = CustomUser.objects.filter(id=user_id)            
#         except CustomUser.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND) 

#         serializer =BuyerSerializer(data = request.data ,many= True)
#         request['user_id'] =user.id
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class RegisterBuyer(APIView):

    
#     def post(self, request, *args, **kwargs):

        
#         if request.method == 'POST':
#             serializer = RegistrationSerializer(data=request.data)
#             data = {}
#             if serializer.is_valid():
#                 account = serializer.save()
#                 for i in request.FILES.getlist('name','about'):
#                     buyer = BuyerSerializer(data=request.data)
#                     if buyer.is_valid():
#                         buyerinfo(account,i)
#                 data['response'] = "successfully registered a new user."
#                 data['email'] = account.email
#                 data['response'] = account.username
#             else:
#                 data = serializer.errors
#                 # data = serializer.data
#             return Response(data)


# def buyerinfo(user_id,info):
#     new_buyer = Buyer.objects.create(user_id=user_id,name=info,about= info)
#     new_buyer.save()
#     return new_buyer






# class BuyerLogin(APIView):

#     def post(self, request):
#         try:
#             email = request.data.get('email')
#             password = request.data.get('password')
#             validate = authenticate(email= email, password = password)

#             if validate:
#                 login(request, validate)
#                 us = CustomUser.objects.get(email = email)
#                 data =  {   'id': us.id,
#                         'token' : validate.auth_token.key,
#                         'email' : request.data['email']
#                     }
                    
#                 return Response(
#                  data, status.HTTP_200_OK
#                 )
#             else:
#                 return Response('Invalid Login', status = status.HTTP_401_UNAUTHORIZED)
#         except Exception as e:
#             return Response(str(e), status = status.HTTP_400_BAD_REQUEST)


