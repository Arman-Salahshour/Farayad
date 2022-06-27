from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny


class MixinSetCookie():

    def _set_token_on_cookie(self, response):
        '''Set cookie if there is access token'''
        access=response.data.get('access')
        if access:
            response.set_cookie(key='jwt', value=access, httponly=True)
        return response

    def post(self, request, *args, **kwargs):
        response=super().post(request, *args, **kwargs)
        response = self._set_token_on_cookie(response)
        print(response)
        return response


class ModifiedTokenObtainPairView(MixinSetCookie, TokenObtainPairView):
    pass

class ModifiedTokenRefreshView(MixinSetCookie, TokenRefreshView):
    pass

