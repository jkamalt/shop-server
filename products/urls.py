from django.urls import path

from products.views import ProductListView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),  # /products/
    path('<int:category_id>/', ProductListView.as_view(), name='category'),  # /products/category_id/
    path('page/<int:page>/', ProductListView.as_view(), name='page'),  # /products/page/<page_num>/
]
