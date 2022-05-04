from django.shortcuts import render
from .models import Invoice, Items

# Create your views here.
def HomeView(request):
    invoiceslist = Invoice.objects.all()
    context = {
        'invoiceslist':invoiceslist
    }
    return render(request, 'index.html', context)

def InvoiceView(request):
    return render(request, 'invoice.html')