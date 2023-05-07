from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Address
from .serializers import AddressSerializer
from users.permissions import IsAccountOwner


class AddressView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer) -> None:
        serializer.save(user=self.request.user)


class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
