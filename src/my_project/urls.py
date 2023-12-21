from django.contrib import admin
from django.urls import path, include
from .base_views import HealthCheckView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/health-check", HealthCheckView.as_view()),
    path("api/v1/", include("user.urls")),
    path("api/v1/", include("my_app.urls")),
]
