
from rest_framework import serializers
from todoapp.models import userDetail,taskDetail

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=userDetail
        fields='__all__'
        
class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model=taskDetail
        fields='__all__'