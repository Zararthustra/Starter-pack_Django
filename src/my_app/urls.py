from django.urls import path
from .my_views import MyGlobalView, MyDetailView

urlpatterns = [
    path("my-endpoint", MyGlobalView.as_view()),
    path("my-endpoint/<str:resource_id>", MyDetailView.as_view()),
]
