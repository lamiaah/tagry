from rest_framework import serializers
from noti.models import Noti


class NotiSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only = True)
    user_id = serializers.PrimaryKeyRelatedField(read_only = True)
    send_at = serializers.DateTimeField(read_only=True)
    image = serializers.ImageField(read_only =True)
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)



    class Meta:
        model=Noti
        fields =['id','user_id','send_at','image','title','description']