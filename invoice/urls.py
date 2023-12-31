from django.urls import path,include
from rest_framework import routers
from invoice import views

router = routers.DefaultRouter()
router.register(r'invoices',views.InvoiceViewset)
router.register(r'invoice-detail',views.InvoiceDetailViewset)

urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += router.urls