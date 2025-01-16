from rest_framework import serializers

from store.models import Store, Product, Customer


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'title']


class ProductSerializer(serializers.ModelSerializer):
    store = StoreSerializer()
    class Meta:
        model = Product
        fields = ['id', 'title', 'store', 'price', 'quantity_in_stock']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user_id', 'first_name', 'last_name']

