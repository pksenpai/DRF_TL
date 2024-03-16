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


#_____________________________________________________________________CBV_Example________________
class PostsListAPIView(APIView):
    permission_classes = [AllowAny,]
    
    def get(self, request):
        posts = Post.objects.all()
        if posts:
            serialized_posts = PostSerializer(instance=posts, many=True).data
            
            return Response(serialized_posts, status=status.HTTP_200_OK)
        return Response({'message': "no posts found!:("}, status=status.HTTP_404_NOT_FOUND)


""" CBV API CRUD """
class CreatePostAPIView(APIView): #C
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser]
    
    def post(self, request):
        # reqest.POST | request.FILES --> can be use too!
        data = request.data # request Body data
        serialized_data = PostSerializer(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


class ReadPostAPIView(APIView): #R
    permission_classes = [AllowAny,] # AllowAny is by default permission on hole project!
    
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        if post:
            serialized_post = PostSerializer(instance=post)
            
            return Response(serialized_post.data, status=status.HTTP_200_OK)
        return Response({'message': "page not found!:("}, status=status.HTTP_404_NOT_FOUND)
        
    
class UpdatePostAPIView(APIView): #U
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]
    
    def put(self, request, pk):
        post = Post.objects.get(pk=pk)
        if post:
            serialized_post = PostSerializer(instance=post, data=request.data, partial=True)
            if serialized_post.is_valid():
                serialized_post.save()
                
                return Response(serialized_post.data, status=status.HTTP_200_OK)
            return Response(serialized_post.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': "post not found!:("}, status=status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, pk):
        post = Post.objects.get(pk=pk)
        if post:
            serialized_post = PostSerializer(instance=post, data=request.data, partial=True)
            if serialized_post.is_valid():
                serialized_post.save()
                
                return Response(serialized_post.data, status=status.HTTP_200_OK)
            return Response(serialized_post.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': "post not found!:("}, status=status.HTTP_404_NOT_FOUND)

    
class DeletePostAPIView(APIView): #D
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]

    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        if post:
            post.delete()
            return Response({'message': "post deleted!:p"}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': "post not found!:("}, status=status.HTTP_404_NOT_FOUND)
                

#______________________________________________________________________FBV_Example____________________
""" FBV API CRUD """
@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BaseAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly,])
def create_post_view(request): #C
    serialized_data = PostSerializer(data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view() # by default only GET method is available
@permission_classes([IsAdminUser,])
def read_post_view(request, pk): #R
    post = Post.objects.get(pk=pk)
    if post:
        serialized_post = PostSerializer(instance=post)
        
        return Response(serialized_post.data, status=status.HTTP_200_OK)
    return Response({'message': "page not found!:("}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT', 'PATCH'])
def update_post_view(request, pk): #U
    post = Post.objects.get(pk=pk)
    if post:
        serialized_post = PostSerializer(instance=post, data=request.data, partial=True)
        if serialized_post.is_valid():
            serialized_post.save()
            
            return Response(serialized_post.data, status=status.HTTP_200_OK)
        return Response(serialized_post.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': "post not found!:("}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_post_view(request, pk): #D
    post = Post.objects.get(pk=pk)
    if post:
        post.delete()
        return Response({'message': "post deleted!:p"}, status=status.HTTP_404_NOT_FOUND)
    return Response({'message': "post not found!:("}, status=status.HTTP_404_NOT_FOUND)

#_____________________________________________________________________UnitView_Example________________
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
            
            return Response(serialized_post.data, status=status.HTTP_200_OK)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk):
        post = Post.objects.get(pk=pk)
        serialized_post = PostSerializer(instance=post, data=request.data, partial=True)
        if serialized_post.is_valid():
            serialized_post.save()
            
            return Response(serialized_post.data, status=status.HTTP_200_OK)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response({'message': "post deleted!"}, status=status.HTTP_200_OK)
    
