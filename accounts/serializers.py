from rest_framework import serializers
from django.contrib.auth.models import User


def email_validator(value: str) -> None:
    if 'admin' in value.lower():
        error = "sorry, admin can't be in email!"
        raise serializers.ValidationError(error)

class UserRegisterSerializer(serializers.Serializer):
    """ auto validate & auto error """
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[email_validator])
    password = serializers.CharField(
        required=True,
        write_only=True, # write_only means that this field only allows writing, not reading!
    ) 
    password2 = serializers.CharField(
        required=True,
        write_only=True, # write_only means that this field only allows writing, not reading!
    ) 
    
    def create(self, validated_data):
        """ override create method """
        del validated_data['password2'] # This is just a checker, but not among the model fields!
        return User.objects.create_user(**validated_data)
        # create_user include with set_password() method so don't worry about hashing password!
    
    def validate_username(self, value: str) -> str:
        if 'admin' in value.lower():
            error = "sorry, admin can't be in username!"
            raise serializers.ValidationError(error)
        
        return value # value must be return
    
    def validate(self, data: dict) -> dict:
        if data['password'] != data['password2']:
            error = "password's not match!"
            raise serializers.ValidationError(error)
        
        return data # data must be return


class UserRegisterModelSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        # fields = '__all__' # all fields without exception!
        fields = ('username', 'email', 'password', 'password2') # choosen fields by tuple or list
        # excludes = ('email',) # all fields exclude email!
        
        extra_kwargs = { # add extra options to serializer fields
            'password': {'write_only': True},
            'email': {'validators': (email_validator,)}
        }
    
    def create(self, validated_data): # fields='__all__' don't work with this!!! why?! %%%BUG%%%?
        """ override create method """
        del validated_data['password2'] # This is just a checker, but not among the model fields!
        return User.objects.create_user(**validated_data)
        # create_user include with set_password() method so don't worry about hashing password!
    
    def validate_username(self, value: str) -> str:
        if 'admin' in value.lower():
            error = "sorry, admin can't be in username!"
            raise serializers.ValidationError(error)
        
        return value # value must be return

    def validate(self, data: dict) -> dict:
        if data['password'] != data['password2']:
            error = "password's not match!"
            raise serializers.ValidationError(error)
        
        return data # data must be return
    
