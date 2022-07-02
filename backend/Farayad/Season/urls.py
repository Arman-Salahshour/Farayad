from django.urls import path
from .views import SeasonsListView, SeasonView


urlpatterns = [
    path('list/<int:pk>/', SeasonsListView.as_view()),
    path('item/<int:pk>/', SeasonView.as_view()),
]
