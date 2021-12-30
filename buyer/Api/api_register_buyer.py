# from buyer.Api.serializer import BuyerSerializer
# from buyer.models import Buyer



# def register_buyer_user(request_data):

#     # 0 initial value
#     # 1 means user already exist
#     # 2 means serializer error
#     # 3 means serializer valid
#     # 4 some thing went wrong

#     response_data = {
#         'error_code' : 0,
#         'serializer_msg' : '',
#     }

#     try:
#         company_user_exist = check_buyer_user_exist(request_data['user'])
#         print("pppo")

#         if company_user_exist == None:
#             print("gg")
#             serializer = BuyerSerializer(data = request_data)
#             if serializer.is_valid() == True:
#                 serializer.save()
#                 response_data['error_code'] = 3
#                 response_data['serializer_msg'] = serializer.data
#                 return response_data
#             else:
#                 response_data['error_code'] = 2
#                 response_data['serializer_msg'] = serializer.error_messages
#                 print("owwwww")
#                 print(serializer.errors)
#                 return response_data
#         else:
#             response_data['error_code'] = 1
#             response_data['serializer_msg'] = 'user exist'
#             print("lllllllllll")
#             return response_data
#     except Exception as e:
#         print(f'-----{e}')
#         response_data['error_code'] = 4
#         response_data['serializer_msg'] = str(e)
#         return response_data




# def check_buyer_user_exist(user_id):

#     try:
#         user = Buyer.objects.get(user = user_id)
#         return user
#     except Exception as e:
#         return None