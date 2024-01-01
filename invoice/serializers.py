from rest_framework import serializers
from .models import Invoice,InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
        
    invoice_detail = InvoiceDetailSerializer(many=True,read_only=True)