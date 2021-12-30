from datetime import date
from users.Api.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.views import APIView
from django.contrib.auth import authenticate, logout, login
from users.models import CustomUser
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from django.views.decorators.csrf import csrf_exempt


class RegisterAPI(APIView):

    
    def post(self, request, *args, **kwargs):
        
        if request.method == 'POST':
            serializer = RegistrationSerializer(data=request.data)
            data = {}
            serializer.is_valid(raise_exception=True)
            if CustomUser.objects.filter(id=data['id']).exists():
                user =CustomUser.objects.get(id=data['id'])
                is_new = "false"
                resp_status = status.HTTP_200_OK
            else:
          
                user = CustomUser.objects.create(id=data['id'],
                                        username=data[' username'],
                                        email=data['email'],
                                        password=data['password'],
                                        )
                user.save()
                is_new = "true"
                resp_status = status.HTTP_201_CREATED
            resp = {"user": serializer.get_serialized(user),
                    "isnew": is_new}
            return Response(resp, status=resp_status)



            # if serializer.is_valid():
            #  


        # data = serializer.data

        # if CustomUser.objects.filter(id=data['id']).exists():
        #     user =CustomUser.objects.get(id=data['id'])
        #     is_new = "false"
        #     resp_status = status.HTTP_200_OK
        # else:
        #     user = CustomUser.objects.create(id=data['id'],
        #                                username=data[' username'],
        #                                email=data['email'],
        #                                password=data['password'],
        #                                )
        #     user.save()
        #     is_new = "true"
        #     resp_status = status.HTTP_201_CREATED
        # resp = {"user": serializer.get_serialized(user),
        #         "isnew": is_new}
        # return Response(resp, status=resp_status)



# class UserLogin(APIView):

#     def post(self, request):
#         try:
#             email = request.data.get('email')
#             password = request.data.get('password')
#             validate = authenticate(email= email, password = password)

#             if validate:
#                 login(request, validate)
#                 us = CustomUser.objects.get(email = email)
#                 return Response(
#                     {   'id': us.id,
#                         'token' : validate.auth_token.key,
#                         'email' : request.data['email']
#                     },
#                     status.HTTP_200_OK
#                 )
#             else:
#                 return Response('Invalid Login', status = status.HTTP_401_UNAUTHORIZED)
#         except Exception as e:
#             return Response(str(e), status = status.HTTP_400_BAD_REQUEST)




# class UserData(APIView):

#     permission_classes = [IsAuthenticated]

#     def get(self, request, pk):

#         try:
#             user_data = CustomUser.objects.get(pk = pk)
#             serializer = UserSerializer(user_data)
#             return Response(serializer.data, status.HTTP_200_OK)
#         except CustomUser.DoesNotExist:
#             return Response(
#                 {
#                     'error' : 'no user found',
#                 },
#                 status.HTTP_404_NOT_FOUND
#             )



# class UserLogout(APIView):

#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         try:
#             logout(request)
#             request.auth.delete()
#             return Response('Success', status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'error' : str(e)}, status.HTTP_406_NOT_ACCEPTABLE)





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
