from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status

from .models import MyModel


class ToolkitService():
    """
        Toolkit service class
    """

    def paginate(*, page_number: int, range: int, records: list[object]):
        """
            Paginate queryset

            Returns: pagination tuple
        """

        paginated_records = Paginator(records, range)
        total_records = paginated_records.count
        page = paginated_records.get_page(page_number)
        has_next = page.has_next()
        start_index = page.start_index()
        end_index = page.end_index()
        return page, has_next, start_index, end_index, total_records


class MyService():
    """
        My service class
    """

    def list():
        """
            List

            Returns: Records
        """
        records = MyModel.objects.all().order_by('-created_at')

        return records

    def detail(*, id: str):
        """
            Detail

            Returns: Record, Status
        """
        try:
            record = MyModel.objects.get(id=id)
            return record, status.HTTP_200_OK
        except Exception as e:
            print(e)
            return None, status.HTTP_404_NOT_FOUND

    def create(*, data: object):
        """
            Create if not exist

            Returns: JSON, Status
        """
        record, created = MyModel.objects.get_or_create(
            name=data["name"],
        )
        if not created:
            return {
                "error": f"Record '{record.name}' with ID '{record.id}' already exists."
            }, status.HTTP_400_BAD_REQUEST
        return {
            "message": f"Record '{record.name}' created successfully."
        }, status.HTTP_201_CREATED

    def update(*, id: str, data: object):
        """
            Update any field from given data

            Returns: Record, Status
        """
        try:
            record = MyModel.objects.get(id=id)
            for key, value in data.items():
                if hasattr(record, key):
                    setattr(record, key, value)
            record.save()
            return record, status.HTTP_200_OK
        except ObjectDoesNotExist:
            return None, status.HTTP_404_NOT_FOUND
        except Exception as e:
            print(e)
            return None, status.HTTP_500_INTERNAL_SERVER_ERROR

    def delete(*, id: str):
        """
            Delete by id

            Returns: Status
        """
        try:
            record = MyModel.objects.get(id=id)
            record.delete()
            return status.HTTP_204_NO_CONTENT
        except Exception as e:
            print(e)
            return status.HTTP_404_NOT_FOUND
