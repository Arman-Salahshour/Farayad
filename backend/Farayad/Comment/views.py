from rest_framework import status
from rest_framework import filters
from rest_framework import generics, mixins
from rest_framework.response import Response
from .models import Course, Payment, Comment
from .serializers import CommentSerializer, PostCommentSerializer
from rest_framework.permissions import IsAuthenticated
from Core.token_authentications import Authentication
from Season.views import access_course
# Create your views here.

'''
request: comment/list/<int:pk> => pk is course's id
request: comment/send/ => post method
'''

class CommentView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (filters.OrderingFilter, )
    lookup_field = 'pk'


class CommentListView(CommentView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.pop('pk')
        queryset = self.get_queryset()
        queryset = queryset.filter(course=pk)
        queryset = self.filter_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CommentPost(CommentView, mixins.CreateModelMixin):
    serializer_class = PostCommentSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (Authentication, )

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        
        course_id = data.get('course')
        course = Course.objects.get(id = course_id)
        author = course.author.id

        if user.id == int(data.get('user')):
            print(user.id, data.get('user'))
            result = access_course(user, author, course, Payment)
            if result == True:
                return self.create(request, *args, **kwargs)
            else:
                return result
        else:
            return Response({
                'message': 'The comment can only be registered by the user who sends the request.'
            }, status = status.HTTP_201_CREATED)