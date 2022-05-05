from .models import Invoice, Items
from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = [
            'item_name',
            'item_quantity',
            'item_price',
        ]

class InvoiceSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = [
            'customer_name',
            'customer_phone',
            'customer_address',
            'invoice_id',
            'invoice_date',
            'items'
        ]

class InvoiceDetailSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = [
            'invoice_id',
            'items'
        ]