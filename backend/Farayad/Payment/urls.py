from django.urls import path
from .views import PaymentListView, PaymentPost
# from Core.token_views import TokenRefreshView

urlpatterns = [
    path('list/', PaymentListView.as_view()),
    path('record/', PaymentPost.as_view()),
]
