# from users.Api.serializers import CustomUserSerializer
# from users.models import CustomUser

# from rest_framework.generics import GenericAPIView
# from rest_framework.response import Response
# from rest_framework import status




# # class RegisterView(GenericAPIView):
# #     serializer_class = CustomUserSerializer

# #     def post(self, request):
# #         serializer = CustomUserSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)

# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# def register(request_data):

#     # 0 initial value
#     # 1 means user already exist
#     # 2 means serializer error
#     # 3 means serializer valid
#     # 4 some thing went wrong

#     response_data = {
#         'error_code' : 0,
#         'serializer_msg' : '',
#     }
#     # get the user id from serializer and all will be finished إن شاء الله 

#     try:
#         user_exist = check_user_exist(request_data['email'])

#         if user_exist == None:
#             serializer = CustomUserSerializer(data = request_data)
#             if serializer.is_valid() == False:
#                 response_data['error_code'] = 2
#                 response_data['serializer_msg'] = serializer.error_messages
#                 return response_data
#             else:
#                 serializer.save()
#                 response_data['error_code'] = 3
#                 response_data['serializer_msg'] = str(serializer.data['id'])
                
#                 return response_data
#         else:
#             response_data['error_code'] = 1
           
#             response_data['serializer_msg'] = str(user_exist.id)
            
#             return response_data
#     except Exception as e:
#         response_data['error_code'] = 4

#         response_data['serializer_msg'] = str(e)
#         return response_data


# def check_user_exist(user_email):

#     try:
#         user = CustomUser.objects.get(email = user_email)
#         print(user)
#         return user
#     except CustomUser.DoesNotExist:
#         return None