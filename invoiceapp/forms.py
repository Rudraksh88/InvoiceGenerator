from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Invoice, Items

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

class ItemForm(ModelForm):
    class Meta:
        model = Items
        fields = ['item_name', 'item_quantity', 'item_price']

ItemFormSet = inlineformset_factory(Invoice, Items, form = ItemForm)