from rest_framework import serializers
from .models import UserDetail, Product, VendorProduct, Order

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class VendorProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProduct
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"