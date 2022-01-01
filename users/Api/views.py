from datetime import date

from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.views import APIView
from django.contrib.auth import authenticate, logout, login
from users.models import CustomUser
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from django.views.decorators.csrf import csrf_exempt
from users.Api.api_register import validate_token
from users.Api.serializers import  CustomUserSerializer


def login_user(request):
    
    res = {}

    try:
        email = request.data.get('email')
        password = request.data.get('password')
        validate = authenticate(email= email, password = password)

        if validate:
            login(request, validate)
    
            res['token'] = validate.auth_token.key
           
            res['status_code'] = '200'
            res['response_msg'] = 'success login'
            return res
        else:
            res['status_code'] = '401'
            res['response_msg'] = 'Invalid Login'
            return res
    except Exception as e:
        print("oiuytre")
        res['status_code'] = '400'
        res['response_msg'] = str(e)
        return res



# class UserLogout(APIView):

#     permission_classes = [IsAuthenticated]

#     def post(self, request, user_id):
#         try:
#             token_validation = validate_token(request, user_id)
#             if token_validation == True:
#                 logout(request)
#                 # request.auth.delete()
#                 return Response('Success', status.HTTP_200_OK)
#             else:
#                 return Response('invalid data', status = status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({'error' : str(e)}, status.HTTP_406_NOT_ACCEPTABLE)





# class UpdateUserPassword(APIView):

#     permission_classes = [IsAuthenticated]


#     def put(self, request, user_id):

#         try:
#             try:
#                 user_data = CustomUser.objects.get(pk = user_id)
#             except CustomUser.DoesNotExist:
#                 return Response(
#                     {
#                         'error' : 'no user found',
#                     },
#                     status.HTTP_404_NOT_FOUND
#                 )
#             else:
#                 token_validation = validate_token(request)
#                 if token_validation == True:
#                     user_data.set_password(request.data.get('new_password'))
#                     user_data.save()
#                     return Response(
#                         {
#                             'response' : 'password updated success',
#                         },
#                         status.HTTP_200_OK
#                     )
#                 else:
#                     return Response(
#                         {
#                             'error' : 'invalid data',
#                         },
#                         status.HTTP_406_NOT_ACCEPTABLE
#                     )

#         except Exception as e:
#             return Response(
#                 {
#                     'error' : 'some thing went wrong {}'.format(e),
#                 },
#                 status.HTTP_400_BAD_REQUEST
#             )




class UserData(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):

        try:
            user_data = CustomUser.objects.get(pk = pk)
            serializer =  CustomUserSerializer(user_data)
            return Response(serializer.data, status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response(
                {
                    'error' : 'no user found',
                },
                status.HTTP_404_NOT_FOUND
            )



class UserrLogout(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            logout(request)
            request.auth.delete()
            return Response('Success', status.HTTP_200_OK)
        except Exception as e:
            return Response({'error' : str(e)}, status.HTTP_406_NOT_ACCEPTABLE)





# class UpdateUserPassword(APIView):

#     permission_classes = [IsAuthenticated]


#     def post(self, request, pk):

#         try:
#             user_data = CustomUser.objects.get(pk = pk)
#             user_data.set_password(request.data['new_password'])
#             user_data.save()
#             return Response(
#                 {
#                     'response' : 'password update success',
#                 },
#                 status.HTTP_200_OK
#             )

#         except CustomUser.DoesNotExist:
#             return Response(
#                 {
#                     'error' : 'no user found',
#                 },
#                 status.HTTP_404_NOT_FOUND
#             )
