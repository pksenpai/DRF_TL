from rest_framework import serializers

from .models import Post, Comment
from .related_fileds import FullNameRelatedField


class PersonPostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField(min_value=1, max_value=100)
    email = serializers.EmailField()
    
    
class PostSerializer(serializers.ModelSerializer):

    ''' show fullname of user: first_name + last_name '''
    author = FullNameRelatedField(read_only=True) # Custome related field

    ''' show __str__ of related model --> here is str(User) '''
    # author = serializers.StringRelatedField(read_only=True) # only read this related element in json
    
    ''' choose a field of related model '''
    # author = serializers.SlugRelatedField(read_only=True, slug_field='email')

    ''' There are two ways to connect methods to fields '''
    comments = serializers.SerializerMethodField(
        # method_name=comments # --> way1
    )
    
    class Meta:
        model = Post
        fields = '__all__'
        
    def get_comments(self, obj): # get_ + method_name --> way2
        comments = obj.comments.all() # data +.+ related_name +.+ query_method
        return CommentSerializer(instance=comments, many=True).data
    
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

