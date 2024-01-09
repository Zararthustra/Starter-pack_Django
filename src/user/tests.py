from django.urls import reverse
from django.test import TestCase

from .models import User
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class UserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@email.com",
            password="password",
            birthdate="1995-05-12",
        )
        self.login_url = reverse("token_obtain_pair")
        self.reconnect_url = reverse("token_refresh")
        self.register_url = reverse("register")
        self.user_refresh_token = get_tokens_for_user(self.user).get("refresh")

    def test_create_user(self):
        self.assertEqual(self.user.email, "testuser@email.com")

    def test_delete_user(self):
        self.user.delete()
        self.assertEqual(self.user.id, None)

    def test_unauthorized_user(self):
        response = self.client.post(
            "/api/v1/my-endpoint",
            {
                "name": "my value",
            },
        )
        self.assertEqual(response.status_code, 401)

    def test_login_user(self):
        response = self.client.post(
            self.login_url, {"email": "testuser@email.com", "password": "password"}
        )
        self.assertEqual(response.status_code, 200)

    def test_reconnect_user(self):
        response = self.client.post(
            self.reconnect_url, {"refresh": self.user_refresh_token}
        )
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        response = self.client.post(
            self.register_url,
            {
                "email": "newuser@email.com",
                "password": "password",
                "first_name": "xxx",
                "last_name": "xxx",
                "gender": "other",
                "birthdate": "2000-05-12",
                "street": "xxx",
                "postal_code": "xxx",
                "city": "xxx",
                "phone_number": "xxx",
            },
        )
        self.assertEqual(response.status_code, 201)
