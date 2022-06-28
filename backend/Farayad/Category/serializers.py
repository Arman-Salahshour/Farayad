from rest_framework import serializers
from .models import GeneralCategory, Category

class GeneralCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GeneralCategory
        fields = ('id','name')


class SubCategorySerializer(serializers.ModelSerializer):

    parent = GeneralCategorySerializer(source='parent_category')
    class Meta:
        model = Category
        fields = ('id','name','parent')
