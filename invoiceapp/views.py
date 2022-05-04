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

def InvoiceView(request, pk):
    invoice = Invoice.objects.get(invoice_id = pk)
    itemslist = list(Items.objects.filter(invoice = pk))

    total = 0
    for item in list(Items.objects.filter(invoice = pk)):
        total = total + item.item_price * item.item_quantity

    itemdetails = {}
    for item in itemslist:
        itemdetails[item.item_name] = item.item_quantity * item.item_price
    
    context = {
        'customer_name': invoice.customer_name,
        'invoice_id': invoice.invoice_id,
        'invoice_date': invoice.invoice_date,
        'customer_phone': invoice.customer_phone,
        'customer_address': invoice.customer_address,
        'total': total,
        'itemslist': itemslist,
        'itemdetails': itemdetails
    }

    print(context['customer_name'])
    return render(request, 'invoice.html', context)