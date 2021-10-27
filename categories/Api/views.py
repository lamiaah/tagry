from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from categories.models import Categories
from categories.Api.serializers import CategorySerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class CategoryApiList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,requset):

        try:
            category = Categories.objects.all()
            serializer = CategorySerializer(category, many = True)
            return Response(serializer.data)
        except Categories.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    
 

        