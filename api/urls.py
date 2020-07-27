from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from .views import PurchaseViewSet, UsersViewSet, UserHyperViewSet, product_list, ProductDetail


router = routers.DefaultRouter()
#router.register(r'product', ProductViewSet)
router.register(r'purchase', PurchaseViewSet)
router.register(r'users', UsersViewSet)
router.register(r'hyperuser', UserHyperViewSet)


urlpatterns = [
    url(r'', include(router.urls)),
    path('product/', product_list),
    path('product/<int:pk>', ProductDetail.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
