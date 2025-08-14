from rest_framework import serializers
from .models import ProductEntry

class ProductEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductEntry
        fields = ['id', 'name', 'product', 'amount']