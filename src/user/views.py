from .models import User
from .serializers import UserSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.http.request import QueryDict

##################
# Authentication #
##################


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["first_name"] = user.first_name
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(APIView):
    def post(self, request):
        # Serialize
        serialized_data = UserSerializer(data=request.data)
        # Validate
        if not serialized_data.is_valid():
            return Response(
                {"error": serialized_data.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            user_data = request.data.copy()
            # Test case
            if isinstance(user_data, QueryDict):
                user_data = user_data.dict()
            User.objects.create_user(**user_data)
            return Response(
                {"message": "User created successfully"}, status=status.HTTP_201_CREATED
            )
        except Exception as e:
            print(type(e), e)
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
