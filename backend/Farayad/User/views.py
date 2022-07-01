from rest_framework import status
from rest_framework import views
from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework import permissions
from Core import token_authentications
from rest_framework_simplejwt.tokens import RefreshToken
from Core.models import User
from .serializers import RegisterUser_serializer, UserFullSerializer
# Create your views here.

class  RegisterUser(generics.GenericAPIView, mixins.CreateModelMixin):
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
class LogoutUser(views.APIView):
    # permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        data = request.data
        refresh_token = data.get('refresh_token')
        
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
            
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

