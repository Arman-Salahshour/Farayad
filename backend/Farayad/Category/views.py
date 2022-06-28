from re import I
from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.response import Response
from .models import GeneralCategory, Category
from .serializers import GeneralCategorySerializer

# Create your views here.
class CategoriesListView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = GeneralCategory.objects.all()
    serializer_class = GeneralCategorySerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        
    
                    