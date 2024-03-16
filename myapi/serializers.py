from rest_framework import serializers
from .models import Post, Comment


class PersonPostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField(min_value=1, max_value=100)
    email = serializers.EmailField()
    
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

