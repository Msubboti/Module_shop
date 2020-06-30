from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .views import ProductList, ItemUpdate

app_name = 'product'

urlpatterns = [
    path('', ProductList.as_view(template_name="product/ProductList.html"), name='store_offers'),
    path('edit/<int:pk>', ItemUpdate.as_view(), name='edit_item'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
