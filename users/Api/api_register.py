from users.Api.serializers import  CustomUserSerializer
from users.models import CustomUser
from rest_framework.authtoken.models import Token


def register(request_data):

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
        user_exist = check_user_exist(request_data['email'])

        if user_exist == None:
            serializer = CustomUserSerializer(data = request_data)
            if serializer.is_valid() == True:
                serializer.save()
                response_data['error_code'] = 3
                response_data['serializer_msg'] = {}
                response_data['serializer_msg']['user_id'] = serializer.data['id']
                response_data['serializer_msg']['user_name'] = serializer.data['username']
                response_data['serializer_msg']['user_email'] = serializer.data['email']
                return response_data
            else:
                response_data['error_code'] = 2
                response_data['serializer_msg'] = serializer.error_messages
                return response_data
        else:
            response_data['error_code'] = 1
            response_data['serializer_msg'] = {}
            response_data['serializer_msg']['user_id'] = str(user_exist.id)
            response_data['serializer_msg']['user_name'] = user_exist.username
            response_data['serializer_msg']['user_email'] = user_exist.email
            return response_data
    except Exception as e:
        response_data['error_code'] = 4
        response_data['serializer_msg'] = str(e)
        return response_data


def check_user_exist(user_email):

    try:
        user = CustomUser.objects.get(email = user_email)
        return user
    except CustomUser.DoesNotExist:
        return None




def validate_token(request):
    
    try:
        user_token = Token.objects.get(user = request.data.get('user_id'))

        if user_token.user.id == int(request.data.get('user_id')) and str(request.auth) == str(user_token.key):
            return True
        else:
            return False
    except Exception as e:
        print('------{}'.format(e))
        return False