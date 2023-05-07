from django.shortcuts import render
from .models import Cart, ProductCart
from .serializers import CartSerializer, ProductCartSerializer
from products.models import Product
from products.serializers import ProductSerializer

from rest_framework.views import APIView, Response, Request, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import generics


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

        # if product.in_stock >= request.data["quantity"]:
        #     product.in_stock -= request.data["quantity"]
        #     product.save()
        # else:
        #     return Response(
        #         {"message": "Insufficient stock"}, status=status.HTTP_409_CONFLICT
        #     )

        if product.in_stock < request.data["quantity"]:
            return Response(
                {"message": "Insufficient stock"}, status=status.HTTP_409_CONFLICT
            )

        is_in_cart = ProductCart.objects.filter(cart=cart, products=product).first()

        if is_in_cart:
            is_in_cart.quantity += request.data["quantity"]

            if is_in_cart.quantity > product.in_stock:
                return Response(
                    {"message": "Insufficient stock"}, status=status.HTTP_409_CONFLICT
                )

            is_in_cart.save()
            return Response(ProductCartSerializer(is_in_cart).data)

        if not is_in_cart:
            serializer_product_cart = ProductCartSerializer(data=request.data)
            serializer_product_cart.is_valid(raise_exception=True)
            serializer_product_cart.save(cart=cart, products=product)

        return Response(serializer_product_cart.data, status=status.HTTP_201_CREATED)

    def patch(self, request):
        product = Product.objects.filter(name=request.data["name"]).first()
        product_cart = ProductCart.objects.filter(
            cart=request.user.cart, products=product
        ).first()

        if not product_cart:
            return Response(
                {"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )

        if request.data["quantity"] >= product_cart.quantity:
            product_cart.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        product_cart.quantity -= request.data["quantity"]
        product_cart.save()

        return Response(ProductCartSerializer(product_cart).data)


# class CartDetailView(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def delete(self, request, pk):
#         product = Product.objects.filter(pk=pk).first()
#         product_cart = ProductCart.objects.filter(
#             cart=request.user.cart, products=product
#         ).first()

#         if not product_cart:
#             return Response(
#                 {"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND
#             )

#         product_cart.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class CartDetailView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductCartSerializer

    def perform_destroy(self, serializer):
        product = Product.objects.get(pk=self.kwargs["pk"])

        product_cart = ProductCart.objects.filter(
            cart=self.request.user.cart, products=product
        ).first()

        if not product_cart:
            return Response(
                {"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )

        product_cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
