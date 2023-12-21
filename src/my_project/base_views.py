from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from my_app.services import ToolkitService

##################
#   Abstracts    #
##################


class GlobalBaseView(APIView):
    """
    Abstract class for global resource
    """

    service = None
    retrieve_serializer = None
    create_serializer = None
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        user_param = request.query_params.get("user_id")
        page_param = request.query_params.get("page")

        # Sanity check
        if user_param:
            try:
                int(user_param)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Services (list & paginate)
        records = self.service.list()
        page, has_next, start_index, end_index, total_records = ToolkitService.paginate(
            page_number=page_param, range=10, records=records
        )

        # Serialize
        serialized_data = self.retrieve_serializer(page, many=True)

        # Response
        response = {
            "total": total_records,
            "from": start_index,
            "to": end_index,
            "is_last_page": not has_next,
            "data": serialized_data.data,
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        payload = request.data

        # Serialize
        serialized_data = self.create_serializer(data=payload)

        # Validate
        if not serialized_data.is_valid():
            return Response(
                {"error": serialized_data.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        # Service
        data, status_code = self.service.create(data=payload)

        # Response
        return Response(data, status=status_code)


class DetailBaseView(APIView):
    """
    Abstract class for detail resource
    """

    service = None
    retrieve_serializer = None
    update_serializer = None
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, resource_id):
        data = {"message": f"Record with id '{resource_id}' not found."}

        # Service
        record, status_code = self.service.detail(id=resource_id)

        # Serialize
        if status_code == 200:
            data = self.retrieve_serializer(record, many=False).data

        # Response
        return Response(data, status=status_code)

    def patch(self, request, resource_id):
        payload = request.data

        # Serialize In
        serialized_data = self.update_serializer(data=payload)

        # Validate
        if not serialized_data.is_valid():
            return Response(
                {"error": serialized_data.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        # Service
        record, status_code = self.service.update(
            id=resource_id, data=serialized_data.data
        )

        # Serialize Out
        data = self.retrieve_serializer(record, many=False).data

        # Response
        return Response(data, status=status_code)

    def delete(self, request, resource_id):
        data = {}

        # Service
        status_code = self.service.delete(id=resource_id)

        # Response
        if status_code == 404:
            data = {"message": f"Record with id '{resource_id}' not found."}
        return Response(data, status=status_code)


##################
#     Views      #
##################


class HealthCheckView(APIView):
    def get(self, request):
        response = {"message": "OK"}
        return Response(response, status=status.HTTP_200_OK)
