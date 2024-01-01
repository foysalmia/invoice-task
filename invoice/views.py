from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer,InvoiceDetailSerializer
from rest_framework.viewsets import ModelViewSet

class InvoiceViewset(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceDetailViewset(ModelViewSet):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer

