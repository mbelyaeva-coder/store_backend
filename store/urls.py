from rest_framework import routers

from store import views

router = routers.DefaultRouter()
router.register(r'stores', views.StoreViewSet)

urlpatterns = router.urls