from django.urls import path
from .views import MyTokenObtainPairView, RegisterView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("register", RegisterView.as_view()),
    path("login", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/reconnect", TokenRefreshView.as_view(), name="token_refresh"),
]
