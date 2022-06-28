from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):

    description_text = serializers.SerializerMethodField()
    def get_description_text(self, object):
        html = object.description.html
        html = html.replace('"', "'")
        return html


    class Meta:
        model = Course
        fields = (
                    'id',
                    'header',
                    'category',
                    'author',
                    'time',
                    'price',
                    'logo',
                    'requirements',
                    'date_modified',
                    'date_published',
                    'description_text',
                )
