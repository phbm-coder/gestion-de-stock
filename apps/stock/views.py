from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import Product, StockMovement
from .serializers import ProductSerializer, StockMovementSerializer, ProductDetailSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductSerializer

    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        products = Product.objects.filter(quantity__lte=models.F('min_quantity'))
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def movement_history(self, request, pk=None):
        product = self.get_object()
        movements = product.movements.all()
        serializer = StockMovementSerializer(movements, many=True)
        return Response(serializer.data)


class StockMovementViewSet(viewsets.ModelViewSet):
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Update product quantity
        product = serializer.validated_data['product']
        quantity = serializer.validated_data['quantity']
        movement_type = serializer.validated_data['movement_type']

        if movement_type == 'IN' or movement_type == 'RETURN':
            product.quantity += quantity
        else:
            product.quantity -= quantity
        product.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
