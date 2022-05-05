from email import generator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Invoice, Items
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import InvoiceSerializer, ItemSerializer, InvoiceDetailSerializer, InvoiceListSerializer

# Create your views here.
def HomeView(request):
    invoiceslist = Invoice.objects.all()
    invoice_exist = True
    if len(list(invoiceslist)) == 0: invoice_exist = False
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
        'itemstotal': itemstotal,
        'invoice_exist': invoice_exist
    }
    
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

    return render(request, 'invoice.html', context)

@api_view(['GET',])
def InvoiceList(request):
    if request.method == 'GET':
        queryset = Invoice.objects.all()
        serializer_class = InvoiceListSerializer(queryset, many=True)
        return Response(serializer_class.data)


@api_view(['GET',])
def InvoiceDetail(request, pk):
    if request.method == 'GET':
        items_list = Items.objects.filter(invoice = pk)
        serializer_class = ItemSerializer(instance=items_list, many=True)
        return Response(serializer_class.data)

@api_view(['GET',])
def ParticularInvoice(request, pk):
    if request.method == 'GET':
        queryset = Invoice.objects.get(invoice_id = pk)
        serializer_class = InvoiceSerializer(queryset, many=False)
        return Response(serializer_class.data)