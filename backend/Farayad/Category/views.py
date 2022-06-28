from re import I
from django.shortcuts import render
from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.response import Response
from .models import GeneralCategory, Category
from .serializers import GeneralCategorySerializer, SubCategorySerializer

# Create your views here.
class CategoriesListView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = GeneralCategory.objects.all()
    serializer_class = GeneralCategorySerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        

class SubCategoriesView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Category.objects.all()
    serializer_class = SubCategorySerializer

    '''In this class pk is the parent category's ID'''
    pk = None
    def get(self, request, *args, **kwargs):

        self.pk = kwargs.get('pk')
        return self.list(request, *args, **kwargs)    

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)

        if self.pk is not None:
            queryset = queryset.filter(parent_category=self.pk)

        return queryset