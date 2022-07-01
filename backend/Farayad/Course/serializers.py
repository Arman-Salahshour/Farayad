from rest_framework import serializers
from .models import Course


def change_date_format(object, how):
    if object is None:
        return None  
        
    date = object.date_published if how =="published" else object.date_modified
    date = f"{date.date().isoformat()} {date.hour}:{date.minute}"

    return date

class CourseSerializerWithDesc(serializers.ModelSerializer):

    description_text = serializers.SerializerMethodField()
    _date_modified = serializers.SerializerMethodField()
    _date_published = serializers.SerializerMethodField()

    def get_description_text(self, object):
        html = object.description.html
        html = html.replace('"', "'")
        return html
    
    def get__date_published(self, object):
       return change_date_format(object, 'published')

    def get__date_modified(self, object):
       return change_date_format(object, 'modified')

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
                    '_date_modified',
                    '_date_published',
                    'description_text',
                )


class CourseSerializerWithoutDesc(CourseSerializerWithDesc):

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
                    '_date_modified',
                    '_date_published',
                )