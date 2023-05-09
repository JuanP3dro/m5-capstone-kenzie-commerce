from .models import Product
from .serializers import ProductSerializer
from .permissions import SellerPermission

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication


class ProductView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, SellerPermission]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]

    def perform_create(self, serializer) -> None:
        serializer.save(seller=self.request.user)

    def get_queryset(self):
        pk_name = self.request.query_params.get("name")
        pk_category = self.request.query_params.get("category")

        if pk_name:
            queryset = Product.objects.filter(name__icontains=pk_name)
            return queryset
        elif pk_category:
            queryset = Product.objects.filter(category=pk_category)
            return queryset

        return super().get_queryset()


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, SellerPermission]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
