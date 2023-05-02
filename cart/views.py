from django.shortcuts import render
from .models import Cart
from .serializers import CartSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class CartView(ListCreateAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer

class CartDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer

