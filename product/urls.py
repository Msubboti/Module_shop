from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static


from .views import ProductList, ItemUpdate, CreateNewProduct, CreatingPurchases, PurchaseList, ReturnPurchase, ReturningList, QueryApproval

app_name = 'product'

urlpatterns = [
    path('', ProductList.as_view(template_name="product/ProductList.html"), name='store_offers'),
    path('edit/<int:pk>', ItemUpdate.as_view(), name='edit_item'),
    path('create/', CreateNewProduct.as_view(), name='new_product'),
    path('purchase/<int:pk>/new', CreatingPurchases.as_view(), name='new_purchase'),
    path('my_purchase/', PurchaseList.as_view(template_name="product/PurchasesList.html"), name='my_purchases'),
    path('item_back/<int:pk>/return', ReturnPurchase.as_view(), name='return_purchase'),
    path('list_returning/', ReturningList.as_view(template_name="product/ReturningList.html"), name='returning_list'),
    path('deleting_returns/<int:pk>', QueryApproval.as_view(), name='deleting_returns'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
