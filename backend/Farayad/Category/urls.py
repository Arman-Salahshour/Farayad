from django.urls import path
from .views import CategoriesListView
# from Core.token_views import TokenRefreshView

urlpatterns = [
    path('', CategoriesListView.as_view()),
]
