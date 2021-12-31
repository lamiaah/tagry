
from rest_framework.views import APIView
from django.contrib.auth import authenticate, logout, login
from rest_framework.response import Response
from users.models import CustomUser
from rest_framework import status
from buyer.Api.serializer import BuyerSerializer

class BuyerLogin(APIView):

    def post(self, request):
    
        email = request.data.get('email')
        password = request.data.get('password')
        validate = authenticate(email= email, password = password)

        if validate:
            login(request, validate)
            us = CustomUser.objects.get(email = email)
            data =  {'id': us.id,
                    'token' : validate.auth_token.key,
                    'email' : request.data['email']
                }
            x=  data['id']
            if request.method == 'POST':
                user = CustomUser.objects.filter(id= x)
                serializer =BuyerSerializer(data = request.data ,many= True)
                request.data["user_id"] = user.id
                if serializer.is_valid():
                
                    serializer.save()  
                    return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)      
                else:
                
                    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 
        
# class BuyerInfo(APIView):
  
  
#     def post(self, request):
#         # try:
#         #     user = CustomUser.objects.filter(id=user_id)            
#         # except CustomUser.DoesNotExist:
#         #     return Response(status=status.HTTP_404_NOT_FOUND) 

#         if request.method == 'POST':
            
#             serializer =BuyerSerializer(data = request.data ,many= True)
#             request.data["user_id"] = request.user.id
#             if serializer.is_valid():
            
#                 serializer.save()  
#                 return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)      
#             else:
              
#                 return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 
        
       