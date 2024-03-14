from rest_framework import serializers


class UserRegisterSerializer(serializers.Serializer):
    """ auto validate & auto error """
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        required=True,
        write_only=True, # write_only means that this field only allows writing, not reading!
    ) 
    
