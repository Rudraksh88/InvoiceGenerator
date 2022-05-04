from xml.etree.ElementTree import TreeBuilder
from .models import Invoice, Items
from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Items
        fields = [
            'invoice',
            'item_name',
            'item_quantity',
            'item_price',
            'item_id',
        ]
        # extra_kwargs = {
        #     'invoice': {"required": True},
        #     'item_id': {"required": False},
            
        # }

class InvoiceSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    # def get_items(self, Items):
    #     return [ItemSerializer(s).data for s in Items.objects.filter(invoice = self.invoice_id)]

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
        extra_kwargs = {
            'invoice_date': {"required": False},
            'invoice_id': {"required": False},
            'customer_phone': {"required": False},
            'customer_address': {"required": False}
        }