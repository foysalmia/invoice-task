from django.urls import path,include
from rest_framework import routers
from invoice import views

router = routers.DefaultRouter()
router.register(r'invoice',views.InvoiceViewset,basename='invoices')
router.register(r'invoice-detail',views.InvoiceDetailViewset,basename='invoiceDetails')

urlpatterns = [
    path('', include(router.urls))
]
