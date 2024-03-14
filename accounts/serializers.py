from rest_framework import serializers


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

