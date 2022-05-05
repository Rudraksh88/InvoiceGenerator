"""invoiceproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from invoiceapp.views import CreateInvoice, HomeView, InvoiceView, InvoiceList, ParticularInvoice, UpdateInvoice

urlpatterns = [
    path('', HomeView),
    path('invoice/<str:pk>', InvoiceView, name='invoice'),
    path('admin/', admin.site.urls),
    path('api/', InvoiceList),
    # path('api/<str:pk>', InvoiceDetail)
    path('api/<str:pk>', ParticularInvoice),
    path('api-create', CreateInvoice),
    path('api/update/<str:pk>/<str:name>/', UpdateInvoice),
]
