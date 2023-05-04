from django.shortcuts import render
from .models import Cart
from .serializers import CartSerializer, ProductCartSerializer
from products.models import Product
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView, Response, Request, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class CartView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post (self, request: Request):
        cart = Cart.objects.filter(user=request.user).first()
        if not cart:
            serializer_cart = CartSerializer(data=request.user)  
        product = Product.objects.filter(name=request.data['name']).first() 

        serializer_product_cart = ProductCartSerializer(data=request.data)
        serializer_product_cart.is_valid(raise_exception=True)
        serializer_product_cart.save(cart=cart, products=product)
        return Response(serializer_product_cart.data, status=status.HTTP_201_CREATED)
        ...
    

class CartDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer

