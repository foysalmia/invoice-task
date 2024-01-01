from django.contrib import admin
from .models import Invoice,InvoiceDetail

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    search_fields = ['customer_name']
    list_display = ['id', 'customer_name','date']
    list_filter = ['customer_name','date']

@admin.register(InvoiceDetail)
class InvoiceDetailAdmin(admin.ModelAdmin):
    list_display = ['id','quantity','unit_price','price']


