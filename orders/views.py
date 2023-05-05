from django.shortcuts import render
from .models import Order
from products.models import Product
from cart.models import Cart, ProductCart
from .serializers import OrderSerializer
from rest_framework.views import APIView, Response, Request, status

class OrderView(APIView):
    def post(self, request: Request):
        cart = Cart.objects.filter(user_id=request.user.id).first()
        id = cart.id
        cart_user = ProductCart.objects.filter(cart_id=id).first()
        sellers = {}
        for elem in cart_user:
            if sellers[str(elem.products.seller)] not in sellers:
                sellers[str(elem.products.seller)] = []
            
            sellers[str(elem.products.seller)].append(elem.products)
        return_list = []
        for seller, product_list in sellers.items():
            instance_list = []
            for elem in product_list:
                product = Product.objects.get(name=elem.name)
                instance_list.append(product)
            serializer = OrderSerializer(data={'products':instance_list})
            serializer.save(user=request.user)
            return_list.append(serializer.data)
            # if elem.products.seller not in sellers:
            #     serializer = OrderSerializer(data=elem.products) 
            #     sellers.append(elem.products.seller) 
            
            # order = Order.objects.filter(user=request.user)   
            # order.products.add(elem.products)
        cart.delete()
        cart_user.delete()
        
        # serializer.is_valid(raise_exception=True)

        # serializer.save(user=request.user)
        
        return Response({'orders':return_list}, status.HTTP_201_CREATED)

    def get(self, request: Request):
        order = Order.objects.filter(user=request.user)

        return Response(OrderSerializer(order).data)
            
    