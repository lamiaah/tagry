from rest_framework import status
from rest_framework.response import Response
from productkeyword.models import Product_keyword
from rest_framework.views import APIView
from productkeyword.Api.serializers import KeySerializer

class KeyWprdList(APIView):
    def get(self,requset):
        
        try:
            key_word = Product_keyword.objects.all()
            serializer = KeySerializer(key_word, many = True)
            return Response(serializer.data)
        except Product_keyword.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    
 

class AddKey(APIView):
    
    def post(self, request):

        serializer = KeySerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST) 