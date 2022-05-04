from django.db import models
import uuid

class Invoice(models.Model):
    customer_name = models.CharField(max_length = 200, verbose_name='Customer Name')
    customer_phone = models.IntegerField(null = True, blank = True, verbose_name='Customer Phone')
    customer_address = models.TextField(null = True, blank = True, verbose_name='Customer Address')
    invoice_id = models.UUIDField(primary_key = True, unique = True, default=uuid.uuid4, verbose_name='Invoice ID')
    invoice_date = models.DateField(auto_now_add=True, verbose_name='Invoice Date')

    def __str__(self):
        return self.customer_name + ' - ' +str(self.invoice_id)
    
    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'


class Items(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete = models.CASCADE, related_name='invoice')
    item_name = models.CharField(max_length = 200, null = False)
    item_quantity = models.IntegerField()
    item_price = models.IntegerField()
    item_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name = 'Items'
        verbose_name_plural = 'Items'