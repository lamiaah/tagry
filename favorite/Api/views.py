from django.http import Http404
from favorite.models import Favorite
from favorite.Api.serializers import FavoriteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status ,generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class FavoriteApiList(generics.ListAPIView):
    
    permission_classes = [IsAuthenticated]

    serializer_class = FavoriteSerializer

    def get_queryset(self):

       
        fav = Favorite.objects.all()
        for i in fav:
             print(i.is_archived)
        users_id = self.kwargs.get('users_id')
        second = self.request.query_params.get('users_id')
        try:
            return Favorite.objects.filter(users_id=users_id)
        except Favorite.DoesNotExist:
            return Http404
        
  



class PostProduct(APIView):
    
    permission_classes = [IsAuthenticated]
    def post(self, request):
        
        serializer = FavoriteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class Delete(APIView):

    permission_classes = [IsAuthenticated]
    def get_object(self, id):
        try:
            return Favorite.objects.get(id= id)
        except Favorite.DoesNotExist:
            return Http404


    def get(self, request,  id):
        favorite= self.get_object(id)
        serializer = FavoriteSerializer(favorite, context={"request": request})
        return Response(serializer.data)


    def delete(self ,request,id):
        favorite= self.get_object(id)
        if favorite == Http404:
            return  Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            favorite.is_archived = True
            favorite.save()
            return Response(status= status.HTTP_200_OK)        
  

        