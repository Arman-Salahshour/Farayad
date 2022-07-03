from rest_framework import serializers
from .models import Comment
from User.serializers import UserSerializer
from Payment.serializers import change_date_format

class CommentSerializer(serializers.ModelSerializer):

    _date_published = serializers.SerializerMethodField()
    _user = UserSerializer(source = 'user')

    def get__date_published(self, object):
        if object is None:
            return None  
        return change_date_format(object.date_published)

    class Meta:
        model = Comment
        fields = (
                  'id',
                  'text',
                  '_user',
                  'course',
                  '_date_published',
                  )

