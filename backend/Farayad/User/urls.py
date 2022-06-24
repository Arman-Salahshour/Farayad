from django.contrib import admin
from django.urls import path
from .views import RegisterUser, LogoutUser
from Core.token_views import ModifiedTokenObtainPairView as TokenObtainPairView
from Core.token_views import TokenRefreshView

urlpatterns = [
    path('register', RegisterUser.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('login/refresh', TokenRefreshView.as_view()),
    path('logout', LogoutUser.as_view()),
]
