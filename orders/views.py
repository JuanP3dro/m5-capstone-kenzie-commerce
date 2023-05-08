from django.shortcuts import render
from .models import Order
from cart.models import Cart, ProductCart
from .serializers import OrderSerializer
from rest_framework.views import APIView, Response, Request, status
from cart.serializers import ProductCartSerializer, CartSerializer
from users.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class OrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        # cart = Cart.objects.filter(user_id=request.user.id).first()
        # id = cart.id
        # cart_user = ProductCart.objects.filter(cart_id=id).first()

        cart_user = ProductCart.objects.filter(cart=request.user.cart)
        cart = Cart.objects.filter(user=request.user).first()

        sellers = []

        for elem in cart_user:
            if elem.products.seller not in sellers:
                serializer = OrderSerializer(data=elem.products)
                sellers.append(elem.products.seller)

            order = Order.objects.filter(user=request.user).first()
            order.products.add(elem.products)

        for x in cart_user:
            if x.products.seller in sellers:
                ...

        cart.delete()
        cart_user.delete()

        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request):
        # order = Order.objects.filter(user=request.user)

        # return Response(OrderSerializer(order).data)

        # ...

        cart_user = ProductCart.objects.filter(cart=request.user.cart)
        print(CartSerializer(request.user.cart).data)

        return Response(ProductCartSerializer(cart_user, many=True).data)
