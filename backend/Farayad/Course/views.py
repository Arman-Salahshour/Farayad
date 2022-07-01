from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from .serializers import CourseSerializerWithDesc, CourseSerializerWithoutDesc
from Core.pagination import CustomizePagination, PaginationHandlerMixin
from .models import Course
# Create your views here.

'''
requests: course/list/?page=_
requests: course/list/?ordering=column_name :: ascending order
requests: course/list/?ordering=-column_name :: descending order
requests: course/item/<str:header>
'''

class CourseListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializerWithoutDesc
    pagination_class = CustomizePagination
    filter_backends = [filters.OrderingFilter]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CourseView(generics.GenericAPIView, mixins.RetrieveModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializerWithDesc
    lookup_field = 'header'

    def get(self, request, *args, **kwargs):
        self.header = kwargs.get('header', None)
        return self.retrieve(request, *args, **kwargs)
