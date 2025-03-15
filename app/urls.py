from app.views import UserAPIView, UserProfileAPIView
from django.urls import path

urlpatterns = [
    path('user/', UserAPIView.as_view(), name='user'),
    path('user-profile/', UserProfileAPIView.as_view(), name='user-profile'),
]