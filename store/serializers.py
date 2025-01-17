from rest_framework import serializers

from store.models import Store, Product, Customer, StoreImage, ProductImage


class StoreImageSerializer(serializers.ModelSerializer):
    store_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = StoreImage
        fields = ['id', 'image', 'store_id']

    def create(self, validated_data):
        store_image = StoreImage.objects.create(store_id= self.context['store_id'], **validated_data)
        return store_image


class StoreSerializer(serializers.ModelSerializer):
    images = StoreImageSerializer(many=True, read_only=True)
    class Meta:
        model = Store
        fields = ['id', 'title', 'images']


class ProductImageSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'product_id']

    def create(self, validated_data):
        product_image = ProductImage.objects.create(product_id= self.context['product_id'], **validated_data)
        return product_image


class ProductSerializer(serializers.ModelSerializer):
    store = StoreSerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'store', 'price', 'quantity_in_stock', 'category', 'images']

    def create(self, validated_data):
        store_id=self.context['store_id']
        if not Store.objects.filter(id=store_id).exists():
            raise serializers.ValidationError('Store does not exist')
        product = Product(store_id=store_id, **validated_data)
        self.instance = product.save()
        return product


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user_id', 'first_name', 'last_name']

