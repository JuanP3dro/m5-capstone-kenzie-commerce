from .serializers import UserSerializer
from .permissions import IsAccountOwner
from .models import User

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAdminUser,
    IsAdminUser,
)
from rest_framework import generics

from rest_framework.views import APIView, Response, status


class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        return [IsAdminUser()]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserAdminView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateAdminView(APIView):
    def post(self, request):
        user = {
            "username": "admin",
            "email": "admin@admin.com",
            "password": "1234",
        }

        admin = User.objects.create_superuser(**user)

        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
