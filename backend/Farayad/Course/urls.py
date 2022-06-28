from django.urls import path
from .views import CourseView
# from Core.token_views import TokenRefreshView

urlpatterns = [
    path('list/', CourseView.as_view()),
]
