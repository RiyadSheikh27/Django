from django.urls import path
from .views import ProductEntryAPIView

urlpatterns = [
    path('products/', ProductEntryAPIView.as_view(), name='product-api'),
]