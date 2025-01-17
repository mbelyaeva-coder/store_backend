from rest_framework_nested import routers
from rest_framework_nested.routers import NestedDefaultRouter

from store import views

router = routers.DefaultRouter()
router.register(r'stores', views.StoreViewSet, basename='stores')
router.register(r'customers', views.CustomerViewSet, basename='customers')

stores_router = routers.NestedDefaultRouter(router, r'stores', lookup='store')
stores_router.register(r'products', views.ProductViewSet, basename='store-products')
stores_router.register(r'images', views.StoreImageViewSet, basename='store-images')

products_router = NestedDefaultRouter(stores_router, r'products', lookup='product')
products_router.register(r'images', views.ProductImageViewSet, basename='product-images')

urlpatterns = router.urls+stores_router.urls+products_router.urls