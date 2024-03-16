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
        
    # def create(self, validated_data: dict) -> object:
    #     return \
    #         Post.objects.create(
    #             author=validated_data['author'],
    #             title=validated_data['title'],
    #             slug=validated_data['slug'],
    #             body=validated_data['body'],
    #         )
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

