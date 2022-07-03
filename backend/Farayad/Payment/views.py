from rest_framework import generics, mixins
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Payment, Course
from .serializers import PaymentSerializer, PaymentPostSerializer
from Core.token_authentications import Authentication

# Create your views here.

'''
request: pay/list/
request: pay/record/ :: post method
'''

class PaymentFilter(filters.BaseFilterBackend):
    """
    Filter courses base on categories
    """
    def filter_queryset(self, request, queryset, view):
        user = request.user
        if user:
            return queryset.filter(purchaser=user)
        return queryset

class PaymentView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (Authentication, )
    filter_backends = (PaymentFilter, )


class PaymentListView(PaymentView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PaymentPost(PaymentView):
    serializer_class = PaymentPostSerializer
    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        
        if user.id == int(data.get('purchaser')):
            if user.id != int(data.get('purchaser')):
                return Response({
                    'message': "error!!  The requesting user must be the same as the user in the list."
                }, status = status.HTTP_400_BAD_REQUEST)
            
            return self.create(request, *args, **kwargs)

        else:
            return Response({
                'message': 'The payment can only be registered by the user who sends the request.'
            }, status = status.HTTP_201_CREATED)

