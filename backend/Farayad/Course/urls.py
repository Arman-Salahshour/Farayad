from django.urls import path
from .views import CourseListView, CourseView, CourseViewWithId
# from Core.token_views import TokenRefreshView

urlpatterns = [
    path('list/', CourseListView.as_view()),
    path('item/<str:header>', CourseView.as_view()),
    path('item/<int:pk>', CourseViewWithId.as_view()),
]
