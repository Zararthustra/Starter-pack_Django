from django.urls import reverse
from django.test import TestCase
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User
from .services import MyService


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class MyAppTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@email.com",
            password="password",
            birthdate="1995-05-12",
        )
        self.service = MyService()
        self.global_url = reverse("my_global_endpoint")
        self.token = "Bearer {}".format(get_tokens_for_user(self.user).get("access"))

    def test_views(self):
        # Create
        response = self.client.post(
            self.global_url,
            {"name": "my value"},
            HTTP_AUTHORIZATION=self.token,
        )
        self.assertEqual(response.status_code, 201)

        # Retrieve global
        response = self.client.get(self.global_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("total"), 1)
        resource_id = response.data["data"][0]["id"]

        # Retrieve detail
        response = self.client.get(
            reverse(
                "my_detail_endpoint",
                kwargs={"resource_id": resource_id},
            ),
            HTTP_AUTHORIZATION=self.token,
        )
        self.assertEqual(response.json().get("name"), "my value")

        # Update
        response = self.client.patch(
            reverse(
                "my_detail_endpoint",
                kwargs={"resource_id": resource_id},
            ),
            {"name": "my updated value"},
            content_type="application/json",
            HTTP_AUTHORIZATION=self.token,
        )
        self.assertNotEqual(response.json().get("name"), "my value")
        self.assertEqual(response.json().get("name"), "my updated value")

        # Unauthorized
        response = self.client.patch(
            reverse(
                "my_detail_endpoint",
                kwargs={"resource_id": resource_id},
            ),
            {"name": "my updated value"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 401)

        # Delete
        response = self.client.delete(
            reverse(
                "my_detail_endpoint",
                kwargs={"resource_id": resource_id},
            ),
            HTTP_AUTHORIZATION=self.token,
        )
        self.assertEqual(response.status_code, 204)

        # Not found
        response = self.client.get(
            reverse(
                "my_detail_endpoint",
                kwargs={"resource_id": resource_id},
            ),
            HTTP_AUTHORIZATION=self.token,
        )
        self.assertEqual(response.status_code, 404)

    def test_services(self):
        # create()
        _, status_code = self.service.create(
            data={"name": "my value"},
        )
        self.assertEqual(status_code, 201)
        _, status_code = self.service.create(
            data={"name": "my value"},
        )
        self.assertEqual(status_code, 400)

        # list()
        records = self.service.list()
        self.assertEqual(len(records), 1)
        resource_id = records[0].id

        # detail()
        data, status_code = self.service.detail(id=resource_id)
        self.assertEqual(status_code, 200)
        self.assertEqual(data.name, "my value")

        # update()
        data, status_code = self.service.update(
            id=resource_id, data={"name": "my updated value"}
        )
        self.assertEqual(status_code, 200)
        self.assertEqual(data.name, "my updated value")

        # delete()
        status_code = self.service.delete(id=resource_id)
        self.assertEqual(status_code, 204)
