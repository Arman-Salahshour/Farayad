from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework import authentication, permissions

from Core.models import User
from .serializers import RegisterUser_serializer
# Create your views here.

class  RegisterUser(generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = RegisterUser_serializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        
        users= User.objects.filter(username=data.get('username'))
        if len(users) != 0:
            return Response({
                'Error': f'This username already exists.'
            })

        emails= User.objects.filter(email=data.get('email'))
        if len(users) != 0:
            return Response({
                'Error': f'This eamail already exists.'
            })

        return self.create(request, *args, **kwargs)
    



