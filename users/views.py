from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics

from .serializers import UserSerializer
from .models import User


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    queryset = User.objects.all()
    serializer_class = UserSerializer
