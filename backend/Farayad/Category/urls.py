from django.urls import path
from .views import CategoriesListView, SubCategoriesView
# from Core.token_views import TokenRefreshView

urlpatterns = [
    path('', CategoriesListView.as_view()),
    path('sub/', SubCategoriesView.as_view()),
    path('sub/<int:pk>/', SubCategoriesView.as_view()),
]
