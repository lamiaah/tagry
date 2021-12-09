from rest_framework import status ,generics 
from django.http import Http404 
from rest_framework.response import Response
from review.models import Review
from rest_framework.views import APIView
from review.Api.serializers import ReviewSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated




class ReviewApiList(generics.ListAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        user_id = self.kwargs.get ('user_id')
        try:
            return Review.objects.filter(user_id=user_id)
        except Review.DoesNotExist:
            return Http404    


class ReviewProductList(generics.ListAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        product_id = self.kwargs.get ('product_id')
        try:
            return Review.objects.filter(products_id=product_id)
        except Review.DoesNotExist:
            return Http404



class ReivewView(APIView):
    
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = ReviewSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
class PutReview(APIView):
    
    permission_classes = [IsAuthenticated]
    def get_object(self, id):
        try:
            return Review.objects.get(id=id)
        except Review.DoesNotExist:
            return Http404


    def get(self,request ,id):

        review = self.get_object(id)
        serializer = ReviewSerializer(review , context = {"request":request}) 
        return Response(serializer.data)


    def put(self ,request ,id ):
        review = self.get_object(id)
        serializer = ReviewSerializer(review ,data=request.data , context = {"request":request}) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors ,status= status.HTTP_400_BAD_REQUEST)

    def delete(self,request ,id):
        review= self.get_object(id)
        if review == Http404:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            review.is_archived = True
            review.save()
            return Response(status= status.HTTP_200_OK) 

    
                       




