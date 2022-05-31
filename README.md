# InvoiceApp

An app that creates printable invoices made using Django with APIs powered by Django REST Framework  
[Live Version](https://invoiceappheroku.herokuapp.com/)

Here are some screenshots:

## Dashboard
This is where you can see all the generated invoices. Click on the INVOICE ID or CUSTOMER NAME to see its details

![127 0 0 1_8000_](https://user-images.githubusercontent.com/62953974/171235237-ce43f32e-427a-48cc-9874-991b5c5f8f18.png)


## Invoice Details
Displays details of a particular invoice. The Print Invoice button opens up the browser's print dialog. 

![127 0 0 1_8000_invoice_a693bec2-2f82-46d2-a317-737c25c4f0f0 (2)](https://user-images.githubusercontent.com/62953974/171235305-80967b28-2c53-499b-a58e-926b369fc602.png)


## Django Admin 
Manage and create new Invoices using this interface  

Default Admin credentials:    
Username: ```admin```  
Password: ```admin@123```  

![127 0 0 1_8000_admin_invoiceapp_invoice_](https://user-images.githubusercontent.com/62953974/171235385-654e5ea9-e97a-4df2-8474-8eb36a1cbfc5.png)

![127 0 0 1_8000_admin_invoiceapp_invoice_a693bec2-2f82-46d2-a317-737c25c4f0f0_change_](https://user-images.githubusercontent.com/62953974/171235430-7c59a9ae-0aa9-483d-8144-30291d723703.png)


### Create new Invoice form

invoice_id and invoice_date are generated automatically when an invoice is created.  

![127 0 0 1_8000_create-invoice_](https://user-images.githubusercontent.com/62953974/171235664-436198a6-3ccc-4274-bd02-3820e062da23.png)

![invoiceapp-heroku herokuapp com_admin_invoiceapp_invoice_add_](https://user-images.githubusercontent.com/62953974/167070978-69e153b6-106f-44a2-8647-28763eeed0b6.png)

## API Guide
### API Endpoints
* ```/api/``` GETs list of all invoices  
* ```/api/get-invoice/{invoice_id}/``` GETs details of a specific invoice  
* ```/api/update/{invoice_id}/{item_name}/``` Updates details of a specific item of a specific invoice  
* ```/api/create/``` Creates a new invoice  

### List of all invoices

```/api/```  

![invoiceapp-heroku herokuapp com_api_](https://user-images.githubusercontent.com/62953974/167071170-e1d9e99f-f5bb-4777-be77-0f71bbbdbc17.png)

### Invoice Details

Example:
To get the invoice details of invoice_id ```a8aeb5a8-5498-40fd-9b4f-bb09a7057c71/```  

```/api/get-invoice/a8aeb5a8-5498-40fd-9b4f-bb09a7057c71/```

![invoiceapp-heroku herokuapp com_api_get-invoice_a8aeb5a8-5498-40fd-9b4f-bb09a7057c71_](https://user-images.githubusercontent.com/62953974/167071476-13c3f576-a530-4d1e-8cee-b1a4d9eab01f.png)

### Update Invoice

Example:
To update the item "PC Cabinet" of the invoice_id ```a8aeb5a8-5498-40fd-9b4f-bb09a7057c71/```  

```/api/update/a8aeb5a8-5498-40fd-9b4f-bb09a7057c71/PC Cabinet```

Format of the PUT request body:
```
{
  "item_name": "PC Cabinet",
  "item_quantity": 1,
  "item_price": 200
}
```

![invoiceapp-heroku herokuapp com_api_update_a8aeb5a8-5498-40fd-9b4f-bb09a7057c71_PC%20Cabinet_](https://user-images.githubusercontent.com/62953974/167071497-6096fa4f-82a5-4927-8ec0-271dbf336f85.png)

### Create Invoice
Example:
Format for the POST request body to create invoice  

```/api/create/```

```
{
    "customer_name": "John Doe",
    "customer_phone": 111666,
    "customer_address": "Palo Alto, California",
    "items": [
        {
            "item_name": "PC Cabinet",
            "item_quantity": 1,
            "item_price": 200
        },
        {
            "item_name": "Motherboard",
            "item_quantity": 1,
            "item_price": 1000
        },
        {
            "item_name": "PSU",
            "item_quantity": 1,
            "item_price": 300
        }
    ]
}
```

![invoiceapp-heroku herokuapp com_api_create_](https://user-images.githubusercontent.com/62953974/167071540-77d4b2c2-1055-430d-a7b5-0be53446ce88.png)
