from rest_framework import serializers
from .models import Season
from Course.serializers import change_date_format

class SeasonSerializer(serializers.ModelSerializer):
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
        model = Season
        fields = ('header',
                  'course',
                  '_date_modified',
                  '_date_published',)


class SpecificSeasonSerializer(SeasonSerializer):

    class Meta:
        model = Season
        fields = ('header',
                    'course',
                    'description_text',
                    '_date_modified',
                    '_date_published',)