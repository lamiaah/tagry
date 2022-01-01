from seller_user.Api.serializers import SellerSerializer
from seller_user.models import Seller


def register_seller(request_data):

    # 0 initial value
    # 1 means user already exist
    # 2 means serializer error
    # 3 means serializer valid
    # 4 some thing went wrong

    response_data = {
        'error_code' : 0,
        'serializer_msg' : '',
    }

    try:
        end_user_exist = check_end_user_exist(request_data['user'])

        if end_user_exist == None:
            serializer =  SellerSerializer(data = request_data)
            
            if serializer.is_valid() == True:
                serializer.save()
                print("ooo")
                response_data['error_code'] = 3
                response_data['serializer_msg'] = serializer.data
                return response_data
            else:
                print("ppppppp")
                response_data['error_code'] = 2
                response_data['serializer_msg'] = serializer.error_messages
                return response_data
        else:
            response_data['error_code'] = 1
            response_data['serializer_msg'] = 'user exist'
            return response_data
    except Exception as e:
        print(f'-----{e}')
        
        response_data['error_code'] = 4
        response_data['serializer_msg'] = str(e)
        return response_data




def check_end_user_exist(user_id):

    try:
        user =Seller.objects.get(user = user_id)
        return user
    except Exception as e:
        return None