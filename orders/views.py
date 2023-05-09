from django.core.mail import send_mail
from django.conf import settings

from .models import Order, ProductOrder
from .serializers import (
    OrderSerializer,
    OrderProductSerializer,
    OrderProductSellerSerializer,
)

from products.models import Product
from products.serializers import ProductSerializer
from products.permissions import SellerPermission

from cart.models import Cart, ProductCart

from users.serializers import UserSerializer
from users.serializers import UserSerializer

from rest_framework.views import APIView, Response, Request, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


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

                        if product.in_stock == 0:
                            product.is_avaliable = False

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

        send_mail(
            subject="Pedido Realizado.",
            message="O pedido foi realizado com sucesso!",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[request.user.email],
            fail_silently=False,
        )

        return Response({"orders": return_list}, status.HTTP_201_CREATED)

    def get(self, request: Request):
        order = Order.objects.filter(user=request.user)

        return Response(OrderSerializer(order, many=True).data)


class OrderUpdateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, SellerPermission]

    def patch(self, request, pk):
        product_order = ProductOrder.objects.filter(
            order_id=pk, product__seller_id=request.user.id
        ).first()

        if not product_order:
            return Response(
                {"message": "Order not found."}, status=status.HTTP_404_NOT_FOUND
            )

        status = ["Pedido Realizado", "Pedido em Andamento", "Pedido Concluido"]

        if request.data["status"] not in status:
            return Response({"message": "status invalid"})

        order = Order.objects.filter(pk=pk).first()
        order.status = request.data["status"]
        order.save()

        send_mail(
            subject="Atualização do pedido",
            message="O status do seu pedido foi atualizado!",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[f"{request.user.email}"],
            fail_silently=False,
        )

        return Response(OrderSerializer(order).data)


class OrderGetView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, SellerPermission]

    def get(self, request):
        orders = ProductOrder.objects.filter(product__seller_id=request.user.id)

        orders_id = []

        for order in orders:
            order_id = OrderProductSellerSerializer(order).data["order"]["id"]

            if order_id not in orders_id:
                orders_id.append(order_id)

        all_orders = []

        for id in orders_id:
            order = Order.objects.filter(id=id).first()
            order = OrderSerializer(order).data

            order["products"] = [
                OrderProductSerializer(
                    ProductOrder.objects.get(product=product, order=id)
                ).data
                for product in order["products"]
            ]

            all_orders.append(order)

        return Response(all_orders)
