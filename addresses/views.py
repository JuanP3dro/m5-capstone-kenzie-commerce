from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Address
from .serializers import AddressSerializer


class AddressView(generics.ListCreateAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer) -> None:
        serializer.save(user=self.request.user)


class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
