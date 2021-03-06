from email import generator
from multiprocessing import context
from attr import fields
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Invoice, Items
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import InvoiceSerializer, ItemSerializer, InvoiceListSerializer, InvoiceCreateSerializer
from .forms import InvoiceForm, ItemForm, ItemFormSet
from django.views.generic.edit import CreateView
from django.db import transaction
import uuid


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

@api_view(['GET'])
def InvoiceList(request):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceListSerializer(queryset, many=True)
    return Response(serializer_class.data)

@api_view(['GET'])
def GetInvoice(request, pk):
    queryset = Invoice.objects.get(invoice_id = pk)
    serializer_class = InvoiceSerializer(queryset, many=False)
    return Response(serializer_class.data)

@api_view(['POST'])
def CreateInvoice(request):
    serializer_class = InvoiceCreateSerializer(data = request.data)
    if serializer_class.is_valid():
         serializer_class.save()
    return Response("Invoice Created")

@api_view(['PUT'])
def UpdateInvoice(request, pk, name):
    items = Items.objects.filter(invoice=pk).filter(item_name = name).first()
    serializer_class = ItemSerializer(instance=items, data = request.data)
    if serializer_class.is_valid():
        serializer_class.save()
    return Response(serializer_class.data)

# class CreateInvoiceClass(CreateView):
#     model = Invoice
#     fields = ['customer_name', 'customer_phone', 'customer_address']
#     success_url = reverse_lazy('dashboard')

#     def get_context_data(self, **kwargs):
#         data = super(CreateInvoiceClass, self).get_context_data(**kwargs)
#         if self.request.POST:
#             data['items'] = ItemFormSet(self.request.POST)
#         else:
#             data['items'] = ItemFormSet()
#         return data
    
#     def form_valid(self, form):
#         context = self.get_context_data()
#         items = context['items']
#         with transaction.atomic():
#             self.object = form.save()

#         if items.is_valid():
#             items.instance = self.object
#             items.save()
        
#         return super(CreateInvoiceClass, self).form_valid(form)

def CreateInvoiceForm(request):
    if request.method == 'POST': print(request.POST)
    print('Item Name List: ')
    item_form = ItemForm(request.POST or None)
    invoice_form = InvoiceForm(request.POST or None)
    itemsList = request.POST.getlist('item_name')
    quantityList = request.POST.getlist('item_quantity')
    priceList = request.POST.getlist('item_price')
    # print(itemsList)
    # print(quantityList)
    # print(priceList)
    # print()
    listofitems = list()
    for i in range(0, len(itemsList)):
        listofitems.append((itemsList[i], quantityList[i], priceList[i]))
    
    # print("Invoice ID: " + str(request.POST['invoice_id']))

    if invoice_form.is_valid() and request.method == 'POST':
        # print(str(request.POST['invoice_id']))
        Invoice.objects.create(invoice_id = request.POST['invoice_id'], 
                               customer_name = request.POST['customer_name'],
                               customer_phone = request.POST['customer_phone'] or None,
                               customer_address = str(request.POST['customer_address']))

        for items in listofitems:
            Items.objects.create(invoice = Invoice.objects.get(invoice_id = request.POST['invoice_id']),
                                item_name = items[0],
                                item_quantity = items[1],
                                item_price = items[2])
        
        return HttpResponseRedirect(request.path_info)
        
    context = {
        'item_form': item_form,
        'invoice_form': invoice_form
    }
    return render(request, 'create_form.html', context)
