from rest_framework import serializers
from .models import Product, StockMovement


class ProductSerializer(serializers.ModelSerializer):
    is_low_stock = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'barcode', 'price', 'quantity', 'min_quantity',
                  'category', 'description', 'is_low_stock', 'created_at', 'updated_at']


class StockMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockMovement
        fields = ['id', 'product', 'quantity', 'movement_type', 'reason', 'notes', 'user', 'created_at']


class ProductDetailSerializer(ProductSerializer):
    movements = StockMovementSerializer(many=True, read_only=True)

    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + ['movements']
