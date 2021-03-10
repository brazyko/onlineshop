from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from cart.models import Order

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['ref_code','owner','items','date_ordered','order_status']