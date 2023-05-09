from django.shortcuts import render
from .models import Order, ProductOrder
from products.models import Product
from cart.models import Cart, ProductCart
from .serializers import OrderSerializer, OrderProductSerializer
from rest_framework.views import APIView, Response, Request, status
from cart.serializers import ProductCartSerializer, CartSerializer
from users.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.serializers import ProductSerializer
from users.serializers import UserSerializer
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import generics


class OrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        cart = Cart.objects.filter(user_id=request.user.id).first()

        if not cart:
            return Response({"message": "Empty cart"}, status.HTTP_400_BAD_REQUEST)

        id = cart.id
        cart_user = ProductCart.objects.filter(cart_id=id)

        sellers = {}

        for elem in cart_user:
            user = UserSerializer(elem.products.seller).data

            if str(user["id"]) not in sellers:
                sellers[str(user["id"])] = []

            sellers[str(user["id"])].append(ProductSerializer(elem.products).data)

        return_list = []

        for seller, product_list in sellers.items():
            instance_list = []

            for elem in product_list:
                product = Product.objects.get(name=elem["name"])
                instance_list.append(product)

            order_cart = Order.objects.create(user=request.user)

            for product in instance_list:
                for elem in cart_user:
                    if elem.products.name == product.name:
                        if product.in_stock < 1 or product.in_stock < elem.quantity:
                            return Response(
                                {"message": "Stock insufficient"},
                                status.HTTP_400_BAD_REQUEST,
                            )

                        ProductOrder.objects.create(
                            order=order_cart, product=product, quantity=elem.quantity
                        )

                        product.in_stock -= elem.quantity
                        product.save()
                    continue

            return_legal = OrderSerializer(order_cart).data

            return_legal["products"] = [
                OrderProductSerializer(
                    ProductOrder.objects.get(product=product, order=order_cart)
                ).data
                for product in return_legal["products"]
            ]

            return_list.append(return_legal)

        cart.delete()
        cart_user.delete()

        return Response({"orders": return_list}, status.HTTP_201_CREATED)

    def get(self, request: Request):
        order = Order.objects.filter(user=request.user)

        return Response(OrderSerializer(order).data)

class OrderUpdateView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_update(self, serializer):
        send_mail(
        subject = 'Atualização do pedido',
        message = 'O status do seu pedido foi atualizado!',
        from_email = settings.EMAIL_HOST_USER,
        recipient_list = ['{self.request.user.email}'],
        fail_silently = False
        )
        ...
        