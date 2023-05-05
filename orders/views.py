from django.shortcuts import render
from .models import Order
from cart.models import Cart, ProductCart
from .serializers import OrderSerializer
from rest_framework.views import APIView, Response, Request, status


class OrderView(APIView):
    def post(self, request: Request):
        cart_user = ProductCart.objects.filter(cart=request.user.cart)
        cart = Cart.objects.filter(user=request.user).first()

        sellers = []

        for elem in cart_user:
            if elem.products.seller not in sellers:
                serializer = OrderSerializer(data=elem.products)
                sellers.append(elem.products.seller)

            order = Order.objects.filter(user=request.user).first()
            order.products.add(elem.products)

        for product in cart_user:
            ...

        cart.delete()
        cart_user.delete()

        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request):
        order = Order.objects.filter(user=request.user)

        return Response(OrderSerializer(order).data)

        ...
