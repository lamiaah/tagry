from datetime import date
from django.http.response import Http404
from rest_framework import status ,generics 
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import Products ,Images
from products.Api.serializers import ImageSerializers, ProductSerializer 
from rest_framework.permissions import IsAuthenticated




def add_images_to_products(products):

    for product in products:
        images = Images.objects.filter(product_id = product['id'])
        image_serialzers = ImageSerializers(data = images, many= True)
        image_serialzers.is_valid()
        product['images'] = image_serialzers.data
    return products

class ProductApiList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            product = Products.objects.filter(is_archived=False)
            serializer = ProductSerializer(product, many = True)
            serializer_product = add_images_to_products(serializer.data)
            return Response(serializer_product)
        except Products.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class SearchApiCategory(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    def get(self,request,category_id):
        try:
            product = Products.objects.filter(category_id=category_id,is_archived= False )
            serializer = ProductSerializer(product, many = True)
            serializer_product = add_images_to_products(serializer.data)
            return Response(serializer_product)
        except Products.DoesNotExist:
            return Response( status = status.HTTP_400_BAD_REQUEST)
        



class SearchApiProduct(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class =ProductSerializer

    def get(self,request,product_title):
        try:
           # product_title = self.kwargs.get('product_title')
            #print(product_title)
            product = Products.objects.filter(product_title=product_title ,is_archived=False )
            serializer = ProductSerializer(product, many = True)
            serializer_product = add_images_to_products(serializer.data)
            return Response(serializer_product)
        except Products.DoesNotExist:
            return Response( status = status.HTTP_400_BAD_REQUEST)
        
        
class AddProduct(APIView):

    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            image_data = {
                'image' : request.data['images'],
                'product' : str(serializer.data['id'])
            }
            image_serialzier = ImageSerializers(data = image_data)
            # added_image = add_image(request.data['images'])
            if image_serialzier.is_valid():
                image_serialzier.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

# this will be used after deployment to add list of images for each product dont remove commented code ( Bassel )

# def add_image(images):
#     try:
#         for i in images:
#             image_serializer = ImageSerializers(data = i)
#             if image_serializer.is_valid():
#                 image_serializer.save()
#                 return True
#             else:
#                 return False
#     except:
#         return False




class PutProduct(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self,id):

        try:
            return Products.objects.get(id = id)
        except Products.DoesNotExist:
            return Http404 

    
    def get(self , request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product, context={"request": request})
        image = add_images_to_products(serializer.data)
        return Response(image) 

      
    def put(self,request,id):
       # user = request.user
       # if Products.updated_user == user:
            product = self.get_object(id)
            serializer = ProductSerializer(product ,data=request.data, context={"request": request}) 
            if serializer.is_valid():
                serializer.save()
                image_data ={
                'product': str(serializer.data['id']),
                'image': request.data['images']
                }
                image_serializer = ImageSerializers(data= image_data)
                if image_serializer.is_valid():
                    image_serializer.save()
                    return Response(image_serializer.data, status= status.HTTP_201_CREATED)  
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST) 
            else:
                return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST) 
        # else: 
        #     return Response({'response':"donot have permission"})       


    def delete(self,request, id):
        product= self.get_object(id)
        if product == Http404:
            return Response(status =status.HTTP_400_BAD_REQUEST)
        else:   
            product.is_archived =True
            product.save()
            return Response(status= status.HTTP_200_OK)         
  
        

