
from rest_framework.views import APIView
from django.contrib.auth import authenticate, logout, login
from rest_framework.response import Response
from users.models import CustomUser
from rest_framework import status
from buyer.Api.serializer import BuyerSerializer

class BuyerLogin(APIView):

    def post(self, request):
        try:
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

                return Response(
                 data, status.HTTP_200_OK
                )
            else:
                return Response('Invalid Login', status = status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(str(e), status = status.HTTP_400_BAD_REQUEST)

class BuyerInfo(APIView):
  
  
    def post(self, request):
      
        user = self.context['request'].id          
     

        if request.method == 'POST':
            
            serializer =BuyerSerializer(data = request.data ,many= True)
            request.data["user_id"] = user.id
            if serializer.is_valid():
            
                serializer.save()  
                return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)      
            else:

                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 
        
       