from django.urls import path
from .views import CommentListView, CommentPost


urlpatterns = [
    path('list/<int:pk>/', CommentListView.as_view()),
    path('send/', CommentPost.as_view()),
]
