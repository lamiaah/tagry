

from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.views import APIView
from django.contrib.auth import authenticate, logout, login
from users.models import CustomUser
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from buyer.models import Buyer
from users.Api.api_register import register, validate_token
from buyer.Api.api_register_buyer import register_buyer
from users.Api.views import login_user



class LoginBuyer(APIView):

    def post(self, request):

        try:
            res = login_user(request)

            if res['status_code'] == '200':
                user_ido = CustomUser.objects.get(email = request.data.get('email'))
                user = Buyer.objects.get(user = user_ido.id)
                print("uu")
                res['user_data'] = {
                   
                    'id' : user_ido.id,
                    'email' : user_ido.email,
                    'username' : user_ido.username,
                    'name' : user.name,
                    'about' : user.about,   
                    'address':user.address,
                    
                }
                
                return Response(res, status = status.HTTP_200_OK)
               
            elif res['status_code'] == '401':
               
                return Response(res, status = status.HTTP_401_UNAUTHORIZED)
            else:
                return Response(res, status = status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
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
                print("here2")
                end_user_data = {
                    'user' : custom_user_register['serializer_msg']['user_id'],
                    'name' : request.data.get('name'),
                    'about' : request.data.get('about'),
                    'image' : request.data.get('image'),
                    'area' : request.data.get('area'),
                    'address' : request.data.get('address'),
                    'city' : request.data.get('city'),
                    'country' : request.data.get('country'),
                    
                }
                print("here3")

                end_user_register = register_buyer(end_user_data)

                if end_user_register['error_code'] == 2:
                    print("here3sdfghj")
                    return Response(end_user_register['serializer_msg'], status = status.HTTP_400_BAD_REQUEST)
                elif end_user_register['error_code'] == 4:
                    print("hererrrrrrewsxcvfd")
                    return Response(end_user_register['serializer_msg'], status = status.HTTP_400_BAD_REQUEST)
                elif end_user_register['error_code'] == 1:
                    print("hererrrrrr")
                    return Response(end_user_register['serializer_msg'], status = status.HTTP_400_BAD_REQUEST)
                else:
                    print("hereiiiiiiiiii")
                    end_user_register['serializer_msg']['user_name'] = custom_user_register['serializer_msg']['user_name']
                    return Response(end_user_register['serializer_msg'], status = status.HTTP_201_CREATED)

        except Exception as e:
            return Response(str(e), status = status.HTTP_400_BAD_REQUEST)





class GetBuyerData(APIView):


    permission_classes = [IsAuthenticated]


    def get(self, request, user_id):

        try:
            token_validator = validate_token(request)

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










