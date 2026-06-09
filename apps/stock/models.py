from django.db import models
from django.utils import timezone


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('ELECTRONICS', 'Électronique'),
        ('CLOTHING', 'Vêtements'),
        ('FOOD', 'Alimentation'),
        ('OTHER', 'Autres'),
    ]

    name = models.CharField(max_length=255)
    barcode = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    min_quantity = models.IntegerField(default=5)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.name

    @property
    def is_low_stock(self):
        return self.quantity <= self.min_quantity


class StockMovement(models.Model):
    MOVEMENT_TYPES = [
        ('IN', 'Entrée'),
        ('OUT', 'Sortie'),
        ('ADJUSTMENT', 'Ajustement'),
        ('RETURN', 'Retour'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='movements')
    quantity = models.IntegerField()
    movement_type = models.CharField(max_length=20, choices=MOVEMENT_TYPES)
    reason = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    user = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.product.name} - {self.movement_type}"
