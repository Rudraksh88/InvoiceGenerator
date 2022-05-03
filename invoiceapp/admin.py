from django.contrib import admin
from .models import Invoice, Items

class ItemsInline(admin.TabularInline):
    model = Items

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_id', 'customer_name', 'invoice_date']
    readonly_fields = ['invoice_date']
    search_fields = ['invoice_id', 'customer_name', 'invoice_date']
    inlines = [ItemsInline]

admin.site.register(Invoice, InvoiceAdmin)
# admin.site.register(Items)