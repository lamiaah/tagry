from django.contrib.auth import authenticate
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from noti.models import Noti
from noti.Api.serializers import NotiSerializer
from rest_framework.permissions import IsAuthenticated


class NotiApiList(generics.ListAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class =NotiSerializer

    def get_queryset(self):
        user = self.kwargs.get('user')
        second = self.request.query_params.get('user')
        try:
            return Noti.objects.filter(user_id=user)
        except Noti.DoesNotExist:
            return Http404


        
    