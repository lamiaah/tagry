from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from area.models import Area
from area.Api.serializers import AreaSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AreaApiList(APIView):
    permission_classes =[IsAuthenticated]
    def get(self,requset):
        
        try:
            area = Area.objects.all()
            serializer = AreaSerializer(area, many = True)
            return Response(serializer.data)
        except Area.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    
