from .views import ProductList

app_name = 'users'

urlpatterns = [
    path('products/', ProductList.as_view(template_name="product/ProductList.html"), name='login'),

]