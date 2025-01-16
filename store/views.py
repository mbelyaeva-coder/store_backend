from django.shortcuts import render
from rest_framework import viewsets

from store.models import Store
from store.serializers import StoreSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer