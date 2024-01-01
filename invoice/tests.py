from rest_framework.test  import APITestCase
from rest_framework import status
from django.urls import reverse

class InvoiceAPITest(APITestCase):

    def test_invoice_get_queryset(self):
        url = reverse('invoices-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_invoice_post_queryset(self):
        url = reverse('invoices-list')
        data = {
                "customer_name": "Jahin Khan",
                "date": "2025-12-05"
                }
        response = self.client.post(url,data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

class InvoiceDetailAPITest(APITestCase):
    
    def test_get_queryset(self):
        url = reverse('invoiceDetails-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


