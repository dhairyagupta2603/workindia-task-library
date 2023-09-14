import json

from django.shortcuts import render
from django.forms.models import model_to_dict
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import status

from knox.models import AuthToken

# from products.models import Product
from .serializers import UserLoginSerializer, UserRegisterSerializer, UserSerializer


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        print(user)

        return Response({
            'status': 'Account successfully created',
        'status_code': 200,
        'user_id': UserSerializer(user, context=self.get_serializer_context()).data['id'],
        })
    

class LoginAPIView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            print(user)

            return Response({
                'status': 'Login successful',
            'status_code': 200,
            'user_id': UserSerializer(user, context=self.get_serializer_context()).data['id'],
            'access_token': AuthToken.objects.create(user)[1]
            })
        else:
            return Response({
                'status': 'Incorrect username/password provided. please retry',
                'status_code': 401,
            })




