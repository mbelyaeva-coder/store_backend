from django.db import models
from django.conf import settings


class Store(models.Model):
    title = models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=255)
    store = models.ForeignKey(Store, on_delete=models.PROTECT, related_name='products')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity_in_stock = models.IntegerField()


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    order = models.ForeignKey('Order', on_delete=models.PROTECT)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='orders')
    date = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    created = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
