from django.shortcuts import render
from .models import Invoice, Items

# Create your views here.
def HomeView(request):
    return render(request, 'index.html')

def InvoiceView(request):
    return render(request, 'invoice.html')