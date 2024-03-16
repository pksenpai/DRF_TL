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

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes

from .models import Person
from .serializers import PersonPostSerializer


""" CBV API CRUD """
class CreatePostAPIView(APIView):
    def post(self, request):
        # reqest.POST | request.FILES --> can be use too!
        data = request.data # request Body data
        name, age = data['name'], data['age']
        result = {'name': name, 'age': age}
        
        return Response(result)
        

class ReadPostAPIView(APIView):
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


class UpdatePostAPIView(APIView):...


class DeletePostAPIView(APIView):...


""" FBV API CRUD """
@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BaseAuthentication])
def create_post_view(request):... #C

@api_view() # by default only GET method is available
def read_post_view(request): #R
    return Response({'name': 'PKPY'})

@api_view(['GET', 'PUT', 'PATCH'])
def update_post_view(request):... #U

@api_view(['GET', 'DELETE'])
def delete_post_view(request):... #D

