
from rest_framework.views import APIView
from users.Api.api_register import register
from rest_framework.response import Response
from users.models import CustomUser
from rest_framework import status
from buyer.Api.serializer import BuyerSerializer


class BuyerInfo(APIView):
  
    def post(self, request,pk):
        id = CustomUser.objects.filter(pk=pk)
        serializer =BuyerSerializer(id,data = request.data)
        if serializer.is_valid():
           serializer.instance['user_id'] = id
           serializer.save()        
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
       