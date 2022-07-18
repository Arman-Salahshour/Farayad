from rest_framework import filters
from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.response import Response
from .serializers import SeasonSerializer, SpecificSeasonSerializer
from rest_framework.permissions import IsAuthenticated
from Core.token_authentications import Authentication
from .models import Course, Season, Payment

# Create your views here.
'''
request: season/list/<int:course_id>
request: season/item/<int:season_id>
'''

def access_course(user, author, course, Payment):
        if user.id != author:
            payment = Payment.objects.filter(purchaser = user, course = course)
            if len(payment) == 0:
                return Response({
                    'message': 'You must first purchase this course in order to access it.'} , 
                    status = status.HTTP_404_NOT_FOUND)
            else:
                True
        else: 
            return True


class SeasonsListView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    lookup_field = 'course'

    def get(self, request, *args, **kwargs):
        pk = kwargs.pop('pk')
        queryset = self.get_queryset()
        queryset = queryset.filter(course=pk).order_by('id')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class SeasonView(generics.GenericAPIView, mixins.RetrieveModelMixin):
    queryset = Season.objects.all()
    serializer_class = SpecificSeasonSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (Authentication, )
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        user = request.user
        season_id = kwargs.pop('pk')
        course = Season.objects.get(id = season_id).course
        author = Course.objects.get(id = course.id).author.id
        result = access_course(user, author, course, Payment)
        if result == True:
            return self.retrieve(request, *args, **kwargs)
        else:
            return result


        # if user.id != author:
        #     payment = Payment.objects.filter(purchaser = user, course = course)
        #     if len(payment) == 0:
        #         return Response({
        #             'message': 'You must first purchase this course in order to access it.'} , 
        #             status = status.HTTP_404_NOT_FOUND)