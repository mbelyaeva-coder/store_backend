from rest_framework_nested import routers

from store import views

router = routers.DefaultRouter()
router.register(r'stores', views.StoreViewSet)

stores_router = routers.NestedDefaultRouter(router, r'stores', lookup='store')
stores_router.register(r'products', views.ProductViewSet, basename='store_products')

urlpatterns = router.urls+stores_router.urls