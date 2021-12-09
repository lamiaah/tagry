from rest_framework import serializers, status ,generics 
from django.http import Http404 
from rest_framework.response import Response
from copun.models import Copun
from rest_framework.views import APIView
from copun.Api.serializers import CopunSerializer
from rest_framework.permissions import IsAuthenticated




class CopunList(generics.ListAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = CopunSerializer

    def get(self,request):
        try:
           copun = Copun.objects.all()
           serializer =CopunSerializer(copun,many = True)
           return Response(serializer.data)
        except Copun.DoesNotExist:
            return Http404    
                 


class CopunAdd(APIView):
    
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = CopunSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PutCopun(APIView):
    
    permission_classes = [IsAuthenticated]
    def get_object(self, id):
        try:
            return Copun.objects.get(id=id)
        except Copun.DoesNotExist:
            return Http404


    def get(self,request ,id):

        Copun = self.get_object(id)
        serializer = CopunSerializer(Copun , context = {"request":request}) 
        return Response(serializer.data)


    def put(self ,request ,id ):
        Copun = self.get_object(id)
        serializer = CopunSerializer(Copun ,data=request.data , context = {"request":request}) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors ,status= status.HTTP_400_BAD_REQUEST)

    def delete(self,request ,id):
        Copun= self.get_object(id)
        if Copun == Http404:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            Copun.is_archived = True
            Copun.save()
            return Response(status= status.HTTP_200_OK) 
