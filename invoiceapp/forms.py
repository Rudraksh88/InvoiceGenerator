from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Invoice, Items

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['customer_address'].widget.attrs['cols'] = 50
        self.fields['customer_address'].widget.attrs['rows'] = 1
        self.fields['invoice_id'].widget.attrs['readonly'] = True
        

class ItemForm(ModelForm):
    class Meta:
        model = Items
        fields = ['invoice', 'item_name', 'item_quantity', 'item_price']

ItemFormSet = inlineformset_factory(Invoice, Items, form = ItemForm)