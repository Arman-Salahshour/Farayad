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

