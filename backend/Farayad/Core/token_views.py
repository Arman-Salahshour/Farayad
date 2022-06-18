from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny

class ModifiedTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response=super().post(request, *args, **kwargs)
        
        '''Set cookie if there is access token'''
        access=response.data.get('access')
        if access:
            response.set_cookie(key='jwt', value=access, httponly=True)

        return response