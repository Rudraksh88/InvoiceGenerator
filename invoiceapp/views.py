from django.shortcuts import render
from .models import Invoice, Items

# Create your views here.
def HomeView(request):
    invoiceslist = Invoice.objects.all()
    itemslist = {}
    itemstotal = {}
    for invoice in invoiceslist:
        key = str(invoice.invoice_id)
        itemslist[key] = list(Items.objects.filter(invoice = key))

        total = 0
        for item in list(Items.objects.filter(invoice = key)):
            total = total + item.item_price * item.item_quantity
            itemstotal[key] = total
    
    context = {
        'invoiceslist':invoiceslist,
        'itemslist': itemslist,
        'itemstotal': itemstotal
    }

    print(context['invoiceslist'])
    print(context['itemslist'])
    print(context['itemstotal'])
    return render(request, 'index.html', context)

def InvoiceView(request):
    return render(request, 'invoice.html')