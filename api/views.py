from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer,OrderSerializer
from cart.models import Order
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CartViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().filter(order_status = 'INC')
    serializer_class = OrderSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().filter(order_status = 'INC')
    serializer_class = OrderSerializer