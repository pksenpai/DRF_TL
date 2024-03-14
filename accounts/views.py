from django.shortcuts import render

from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserRegisterSerializer, UserRegisterModelSerializer


class UserRegisterView(APIView): # create user (C in CRUD)
    def post(self, request):
        # serialized_data = UserRegisterSerializer(data=request.POST) # data-> validate data from client
        serialized_data = UserRegisterModelSerializer(data=request.POST) # data-> validate data from client
        if serialized_data.is_valid():
            data: dict = serialized_data.validated_data
            serialized_data.create(data) # Custome create method

            return Response(serialized_data.data)
        return Response(serialized_data.errors) # return serializer auto errors

