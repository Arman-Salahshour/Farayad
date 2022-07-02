from django.contrib import admin
from django.urls import path
from .views import RegisterUser, LogoutUser, GetUserInformation, ChangeUserInformation
from Core.token_views import ( ModifiedTokenObtainPairView as TokenObtainPairView,
                                ModifiedTokenRefreshView as TokenRefreshView )
# from Core.token_views import TokenRefreshView

urlpatterns = [
    path('register', RegisterUser.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('login/refresh', TokenRefreshView.as_view()),
    path('logout', LogoutUser.as_view()),
    path('info', GetUserInformation.as_view()),
    path('update', ChangeUserInformation.as_view()),
]
