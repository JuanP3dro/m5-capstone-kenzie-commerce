from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import SellerPermission


class ProductView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, SellerPermission]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer) -> None:
        serializer.save(seller=self.request.user)

    def get_queryset(self):
        pk_name = self.request.query_params.get("name")
        pk_category = self.request.query_params.get("category")

        if pk_name:
            queryset = Product.objects.filter(name__contains=pk_name)
        elif pk_category:
            queryset = Product.objects.filter(category=pk_category)

        return super().get_queryset()


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, SellerPermission]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
