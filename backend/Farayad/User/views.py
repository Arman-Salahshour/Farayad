from rest_framework import status
from rest_framework import views
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework import permissions
from Core import token_authentications
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken, BlacklistMixin
from Core.models import User
from .serializers import RegisterUser_serializer, UserFullSerializer
from django.contrib.auth.hashers import check_password, make_password
# Create your views here.

'''
request: user/register/
request: user/login/ => post method{username, password}
request: login/refresh/ => post method{refresh}
request: user/logout/ =>post method{refresh} if there is JWT COOKIE just send a post request with empty body.
request: user/info/ => get method(if there is no JWT COOKIE set {Authorization: 'Bearer access token'})
request: user/update/ => put method(you can change user information with this endpoint)
request: user/state/ => get method(if user is admin, it will return 'admin' else if user is ordinary but volunteer 
                        for being admin, it will return 'ordinary but volunteer' else it will return 'ordinary')
request: user/volun/ => get method for requesting to be an admin.
'''

def Check_Password(obj, request):
    match = check_password( request.data.get('current_password'), obj.password)
    return match

class RegisterUser(generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = RegisterUser_serializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        
        users= User.objects.filter(username=data.get('username'))
        if len(users) != 0:
            return Response({
                'Error': f'This username already exists.'
            })

        emails= User.objects.filter(email=data.get('email'))
        if len(users) != 0:
            return Response({
                'Error': f'This eamail already exists.'
            })

        return self.create(request, *args, **kwargs)
    



# """Logout"""

class ModifiedAccessToken(AccessToken, BlacklistMixin):
    pass

class LogoutUser(views.APIView):
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (token_authentications.Authentication, )

    def post(self, request, *args, **kwargs):
        data = request.data
        refresh_token = data.get('refresh')
        access_token = data.get('access')
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

            token = ModifiedAccessToken(access_token)
            token.blacklist()

            response = Response(data={
                'message': 'User has loged out'
            },status=status.HTTP_205_RESET_CONTENT)

            response.delete_cookie('jwt')
            return response
            
        except Exception as e:
            return Response(data={
                'message': 'Token is invalid or expired'
            },status=status.HTTP_400_BAD_REQUEST)


class GetUserInformation(views.APIView):
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (token_authentications.Authentication, )

    def get(self, request, *args, **kwargs):
        user = request.user.id
        user = User.objects.get(id=user)
        serializer = UserFullSerializer(user)

        return Response(serializer.data, status = status.HTTP_200_OK)



class SpecificUserFilter(filters.BaseFilterBackend):
    """
    Find a User who has sent the request
    """
    def filter_queryset(self, request, queryset, view):
        user = request.user.id
        if user:
            return queryset.filter(id=user)
        return queryset

class ChangeUserInformation(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = RegisterUser_serializer
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (token_authentications.Authentication, )
    filter_backends = (SpecificUserFilter, )
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.filter_queryset(self.get_queryset())[0]
        data = request.data

        if data.get('password', None) != None:
            data._mutable = True
            data.update({'password':make_password(data.get('password')),})

        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):   
        return self.partial_update(request, *args, **kwargs)


class UserState(views.APIView):
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (token_authentications.Authentication, )

    def get(self, request, *args, **kwargs):
        user = request.user
        return Response({
            'message': 'admin' if user.is_superuser else 'ordinary but volunteer' if user.is_volunteer else 'ordinary'
        }, status = status.HTTP_200_OK)


class AdminRequestHandler(UserState):
    
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser == False:
            user.is_volunteer = True
            user.save()

        return Response({
            'message': 'admin' if user.is_superuser else 'ordinary but volunteer' if user.is_volunteer else 'ordinary'
        }, status = status.HTTP_200_OK)
