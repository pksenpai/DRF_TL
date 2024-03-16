'''
\_______________________________[STATUS-CODE]__________________________________/

Status BaseCode      Means               Helper Functions
===============      ==============      ===================
1xx                  Informational       is_informational()
2xx                  Successful          is_success()
3xx                  Redirection         is_redirect()
4xx                  Client Error        is_client_error()
5xx                  Server Error        is_server_error()
________________________________________________________________________________/
'''
from django.shortcuts import render

from django.contrib.auth.models import User

from rest_framework.authentication import SessionAuthentication, BaseAuthentication

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserRegisterSerializer, UserRegisterModelSerializer


class UserRegisterView(APIView): # create user (C in CRUD)
    # authentication_classes = [SessionAuthentication, BaseAuthentication] # --> set up the authentication type just for this view
    
    def post(self, request):
        # serialized_data = UserRegisterSerializer(data=request.POST) # data-> validate data from client
        serialized_data = UserRegisterModelSerializer(data=request.POST) # used ModelSerializer 
        if serialized_data.is_valid():
            data: dict = serialized_data.validated_data
            serialized_data.create(data) # Custome create method

            return Response(serialized_data.data, status=status.HTTP_201_CREATED) # status used for more human readable
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST) # .errors return serializer auto errors


# https://www.django-rest-framework.org/api-guide/status-codes/
#_______________________________________________________________________________/
