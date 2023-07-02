from django.urls import path
from .views import my_views
from .views.base_views import MyTokenObtainPairView, HealthCheckView, RegisterView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    # Health check
    path('health-check', HealthCheckView.as_view()),

    # Authentication
    path('register', RegisterView.as_view()),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Views
    path('my-endpoint', my_views.MyGlobalView.as_view()),
    path('my-endpoint/<str:resource_id>', my_views.MyDetailView.as_view()),
]
