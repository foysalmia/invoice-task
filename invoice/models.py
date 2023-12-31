from django.db import models

class Invoice(models.Model):
    customer_name = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self) -> str:
        return  f"{self.id} {self.customer_name} {self.date}"

class InvoiceDetail(models.Model):
    description = models.TextField()
    quantity = models.IntegerField()
    unit_price = models.DecimalField(default=1,max_digits=6,decimal_places=2)
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE,related_name = 'invoice_detail')
    
    @property
    def price(self):
        return self.quantity * self.unit_price


