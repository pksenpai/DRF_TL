from rest_framework import serializers


class PersonPostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField(min_value=1, max_value=100)
    email = serializers.EmailField()
    
    