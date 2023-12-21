from my_project.base_views import GlobalBaseView, DetailBaseView
from .services import MyService
from .serializers import (
    MyRetrieveListSerializer,
    MyRetrieveDetailSerializer,
    MyCreateSerializer,
    MyUpdateSerializer,
)


class MyGlobalView(GlobalBaseView):
    """
    My global resource view
    """

    service = MyService
    retrieve_serializer = MyRetrieveListSerializer
    create_serializer = MyCreateSerializer


class MyDetailView(DetailBaseView):
    """
    My detail resource view
    """

    service = MyService
    retrieve_serializer = MyRetrieveDetailSerializer
    update_serializer = MyUpdateSerializer
