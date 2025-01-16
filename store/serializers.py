from rest_framework import serializers

from store.models import Store, Product


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    store = StoreSerializer()
    class Meta:
        model = Product
        fields = ['id', 'title', 'store', 'price', 'quantity_in_stock']