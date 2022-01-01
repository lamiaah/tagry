
from buyer.Api.serializer import BuyerSerializer
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.views import APIView
from django.contrib.auth import authenticate, logout, login
from users.models import CustomUser
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from users.Api.serializers import RegistrationSerializer
from django.views.decorators.csrf import csrf_exempt
from buyer.models import Buyer

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
        
class BuyerInfo(APIView):
  
  
    def post(self, request ,user_id):
        try:
            user = CustomUser.objects.filter(id=user_id)            
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 

        serializer =BuyerSerializer(data = request.data ,many= True)
        request['user_id'] =user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterBuyer(APIView):

    
    def post(self, request, *args, **kwargs):
        
        
        if request.method == 'POST':
            serializer = RegistrationSerializer(data=request.data)
            data = {}
            if serializer.is_valid():
                account = serializer.save()
                for i in request.FILES.getlist('name','about','address'):
                    buyer = BuyerSerializer(data=request.data)
                    if buyer.is_valid():
                        buyerinfo(account,i)
                data['response'] = "successfully registered a new user."
                data['email'] = account.email
                data['response'] = account.username
            else:
                data = serializer.errors
                # data = serializer.data
            return Response(data)


def buyerinfo(user_id,info):
    new_buyer = Buyer.objects.create(user_id=user_id,name=info,about= info,address= info)
    new_buyer.save()
    return new_buyer






class BuyerLogin(APIView):

    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            validate = authenticate(email= email, password = password)

            if validate:
                login(request, validate)
                us = CustomUser.objects.get(email = email)
                data =  {   'id': us.id,
                        'token' : validate.auth_token.key,
                        'email' : request.data['email']
                    }
                    
                return Response(
                 data, status.HTTP_200_OK
                )
            else:
                return Response('Invalid Login', status = status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(str(e), status = status.HTTP_400_BAD_REQUEST)
