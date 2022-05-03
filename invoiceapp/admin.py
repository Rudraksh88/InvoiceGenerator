from django.contrib import admin
from .models import Invoice, Items

admin.site.register(Invoice)
admin.site.register(Items)