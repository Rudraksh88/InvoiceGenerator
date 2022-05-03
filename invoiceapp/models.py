from django.db import models
import uuid

class Invoice(models.Model):
    customer_name = models.CharField(max_length = 200)
    customer_phone = models.IntegerField(null = True, blank = True)
    customer_address = models.TextField(null = True, blank = True)
    invoice_id = models.UUIDField(primary_key = True, unique = True, default=uuid.uuid5)
    invoice_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item_name

class Items(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete = models.DO_NOTHING)
    item_name = models.CharField(max_length = 200, null = False)
    item_quantity = models.IntegerField()
    item_price = models.IntegerField()
    item_id = models.IntegerField(primary_key=True, unique=True)
