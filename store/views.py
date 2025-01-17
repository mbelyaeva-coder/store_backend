from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from store.models import Store, Product, Customer, StoreImage
from store.serializers import StoreSerializer, ProductSerializer, CustomerSerializer, StoreImageSerializer
from store.permissions import IsAdminOrReadOnly


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAdminOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return Product.objects.filter(store_id=self.kwargs['store_pk'])

    def get_serializer_context(self):
        return {'store_id': self.kwargs['store_pk']}


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsAdminUser]


class StoreImageViewSet(viewsets.ModelViewSet):
    serializer_class = StoreImageSerializer

    def get_queryset(self):
        return StoreImage.objects.filter(store_id=self.kwargs['store_pk'])

    def get_serializer_context(self):
        return {'store_id': self.kwargs['store_pk']}