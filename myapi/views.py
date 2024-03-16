'''
HTTP Methods         CRUD                Example
==============       =============       =================================
POST                 Create              Create a new blog post
GET                  Read                Display a list of posts with pagination 
PUT                  Update/Replace      Replace something in the posts list
PATCH                Update/Modify       Edit something from the list of posts
DELETE               Delete              Delete specific post
________________________________________________________________________________
'''
from django.shortcuts import render

from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from rest_framework.response import Response
from rest_framework import status

from .models import Person, Post, Comment
from .serializers import PersonPostSerializer, PostSerializer, CommentSerializer


class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serialized_posts = PostSerializer(instance=posts, many=True).data
        
        return Response(serialized_posts, status=status.HTTP_200_OK)
        
    def post(self, request):
        serialized_data = PostSerializer(data=request.data) # or request.POST
        if serialized_data.is_valid():
            serialized_data.save()
            
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk):
        post = Post.objects.get(pk=pk)
        serialized_post = PostSerializer(instance=post, data=request.data, partial=True)
        if serialized_post.is_valid():
            serialized_post.save()
            
            return Response(serialized_post.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk):
        post = Post.objects.get(pk=pk)
        serialized_post = PostSerializer(instance=post, data=request.data, partial=True)
        if serialized_post.is_valid():
            serialized_post.save()
            
            return Response(serialized_post.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response({'message': "post deleted!"}, status=status.HTTP_200_OK)
    

















#_________________________________________________________CRUD_EXAMPLES_____________
""" CBV API CRUD """
class CreatePostAPIView(APIView): #C
    permission_classes = [IsAuthenticated,]
    
    def post(self, request):
        # reqest.POST | request.FILES --> can be use too!
        data = request.data # request Body data
        name, age = data['name'], data['age']
        result = {'name': name, 'age': age}
        
        return Response(result)
        

class ReadPostAPIView(APIView): #R
    permission_classes = [AllowAny,] # AllowAny is by default permission on hole project!
    
    def get(self, request, name):
        # 001
        result = {'NAME': name}
        qparam: dict = request.query_params
        result.update(qparam)
        
        # 002
        persons = Person.objects.all()
        serialized_data = PersonPostSerializer(instance=persons, many=True) # use many for queryset
   
        someone = Person.objects.get(name='Parsa', id=1)
        serialized_someone = PersonPostSerializer(instance=someone) # remove many

        ################################
        print(serialized_data)
        print('-'*20)
        print(serialized_data.data)
        ################################
        
        data1 = {'s': serialized_data.data, 'r': result}
        data2 = {'s': serialized_someone.data, 'r': result}
        
        flag = True
        return Response(data=data1 if flag else data2)
    
class UpdatePostAPIView(APIView):... #U
class DeletePostAPIView(APIView):... #D

""" FBV API CRUD """
@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BaseAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly,])
def create_post_view(request):... #C

@api_view() # by default only GET method is available
@permission_classes([IsAdminUser,])
def read_post_view(request): #R
    return Response({'name': 'PKPY'})

@api_view(['GET', 'PUT', 'PATCH'])
def update_post_view(request):... #U

@api_view(['GET', 'DELETE'])
def delete_post_view(request):... #D
#__________________________________________________________________________________________
