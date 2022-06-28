from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer
from Core.pagination import CustomizePagination, PaginationHandlerMixin

# Create your views here.

class CourseView(generics.GenericAPIView, mixins.ListModelMixin, ):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CustomizePagination
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


