from rest_framework import status ,generics 
from  django.http import Http404
from rest_framework.views import APIView
from recently_view.models import Recently_view
from rest_framework.response import Response
from recently_view.Api.serializers import RecentlyViewSerializer
from rest_framework.permissions import IsAuthenticated

class RecentlyViewApiList(generics.ListAPIView):
    permission_classes =[IsAuthenticated]
    serializer_class = RecentlyViewSerializer

    def get_queryset(self):
        user_id = self.kwargs.get ('user_id')
        second = self.request.query_params.get('user_id')


        try:
            return Recently_view.objects.filter(user_id=user_id)
        except Recently_view.DoesNotExist:
            return Http404    


class AddRvie(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request):
        serializer = RecentlyViewSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        