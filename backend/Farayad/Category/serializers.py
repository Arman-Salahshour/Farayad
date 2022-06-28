from rest_framework import serializers
from .models import GeneralCategory

class GeneralCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralCategory
        fields = ('id','name')
