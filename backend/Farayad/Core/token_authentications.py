from rest_framework_simplejwt.authentication import JWTAuthentication

class Authentication(JWTAuthentication):

    def get_COOKIES_token(self,request):
        token = request.COOKIES.get('jwt')
        return token

    def authenticate(self, request):
        raw_token = self.get_COOKIES_token(request)
        if raw_token is None:
            header = self.get_header(request)
            if header is None:
                return None

            raw_token = self.get_raw_token(header)

        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)

        return self.get_user(validated_token), validated_token

