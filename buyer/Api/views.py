from rest_framework.views import APIView
from users.Api.api_register import register
from rest_framework.response import Response
from rest_framework import status
from buyer.Api.api_register_buyer import register_buyer_user


class RegisterBuyer(APIView):

   
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
                    'about' : request.data.get('about'),
                    'address' : request.data.get('address'),
                    'city' : request.data.get('city'),
                    'country' : request.data.get('country'),
                    'image' : request.data.get('image'),
                    'area' : request.data.get('area'),
                  }
               
                buyer_user_register = register_buyer_user(couser_data)
               
                if buyer_user_register['error_code'] == 2:
                    return Response(buyer_user_register['serializer_msg'], status = status.HTTP_400_BAD_REQUEST)
                elif buyer_user_register['error_code'] == 4:
                    return Response(buyer_user_register['serializer_msg'], status = status.HTTP_400_BAD_REQUEST)
                elif buyer_user_register['error_code'] == 1:
                    return Response(buyer_user_register['serializer_msg'], status = status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(buyer_user_register['serializer_msg'], status = status.HTTP_201_CREATED)



        except Exception as e:
            return Response(str(e), status = status.HTTP_400_BAD_REQUEST)
