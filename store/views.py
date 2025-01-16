from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from store.models import Store, Product, Customer
from store.serializers import StoreSerializer, ProductSerializer, CustomerSerializer
from store.permissions import IsAdminOrReadOnly


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    # permission_classes = [IsAdminOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return Product.objects.filter(store_id=self.kwargs['store_pk'])
    # permission_classes = [IsAdminOrReadOnly]


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    # permission_classes = [IsAdminUser]