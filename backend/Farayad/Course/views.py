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
request: course/list/?page=_
request: course/list/?cat=category
request: course/list/?ordering=column_name :: ascending order
request: course/list/?ordering=-column_name :: descending order
request: course/list/?search=(str)&search_field=column_name&search_field=...
request: course/item/<str:header>
'''


class DynamicSearch(filters.SearchFilter,):
    def get_search_fields(self,view, request):
        return request.GET.getlist('search_field',[])

class CategoryFilter(filters.BaseFilterBackend):
    """
    Filter courses base on categories
    """
    def filter_queryset(self, request, queryset, view):
        category = request.query_params.get('cat')
        if category:
            return queryset.filter(category=category)
        return queryset


class CourseListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializerWithoutDesc
    pagination_class = CustomizePagination
    filter_backends = (DynamicSearch, filters.OrderingFilter, CategoryFilter, )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CourseView(generics.GenericAPIView, mixins.RetrieveModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializerWithDesc
    lookup_field = 'header'

    def get(self, request, *args, **kwargs):
        self.header = kwargs.get('header', None)
        return self.retrieve(request, *args, **kwargs)


class CourseViewWithId(CourseView):
    lookup_field = 'id'
