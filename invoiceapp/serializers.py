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

class InvoiceListSerializer(serializers.ModelSerializer):
    # items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = [
            'customer_name',
            'customer_phone',
            'customer_address',
            'invoice_id',
            'invoice_date',
            # 'items'
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
        model = Items
        fields = [
            'invoice_id',
            'items'
        ]

class InvoiceCreateSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Invoice
        fields = [
            'customer_name',
            'customer_phone',
            'customer_address',
            'items'
        ]

        extra_kwargs = {
            'invoice_id': {'required': False },
        }

    def create(self, validated_data):
        invoice_items = validated_data.pop('items')
        invoice = Invoice.objects.create(**validated_data)
        for items in invoice_items:
            Items.objects.create(invoice = invoice, **items)
        return invoice