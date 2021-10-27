from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from languages.models import Languages
from languages.Api.serializers import LanguagesSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class LanguageList(APIView):
    permission_classes =[IsAuthenticated]
    
    def get(self, requset):
        try:
            language = Languages.objects.all()
            serializer=LanguagesSerializer(language, many = True)
            return Response (serializer.data)
        except Languages.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

            
