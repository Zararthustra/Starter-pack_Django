from .base_views import GlobalBaseView, DetailBaseView
from my_app.services import MyService
from my_app.serializers import MyRetrieveListSerializer, MyRetrieveDetailSerializer, MyCreateSerializer, MyUpdateSerializer


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
