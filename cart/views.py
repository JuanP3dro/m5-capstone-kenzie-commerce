from django.shortcuts import render
from .models import Cart, ProductCart
from .serializers import CartSerializer, ProductCartSerializer
from products.models import Product

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView, Response, Request, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class CartView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        product_cart = ProductCart.objects.filter(cart=request.user.cart)

        return Response(ProductCartSerializer(product_cart, many=True).data)

    def post(self, request: Request):
        cart = Cart.objects.filter(user=request.user).first()
        if not cart:
            cart = Cart.objects.create(user=request.user)

        product = Product.objects.filter(name=request.data["name"]).first()

        if not product:
            return Response(
                {"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )

        verify = ProductCart.objects.filter(cart=cart, products=product).first()

        if verify:
            verify.quantity += request.data["quantity"]
            verify.save()
            return Response(ProductCartSerializer(verify).data)

        else:
            if product.in_stock >= request.data["quantity"]:
                product.in_stock -= request.data["quantity"]
                product.save()
            else:
                return Response(
                    {"message": "Insufficient stock"}, status=status.HTTP_409_CONFLICT
                )

            serializer_product_cart = ProductCartSerializer(data=request.data)
            serializer_product_cart.is_valid(raise_exception=True)
            serializer_product_cart.save(cart=cart, products=product)

        return Response(serializer_product_cart.data, status=status.HTTP_201_CREATED)


class CartDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer