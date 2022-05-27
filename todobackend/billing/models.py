from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ISV_Type(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Discount_Type(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Product(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_public_price = models.IntegerField()

class Invoice(models.Model):
    cai = models.CharField(max_length=100)
    datetime_issue = models.DateTimeField(auto_now_add=True)

class Transaction(models.Model):
    reduction = models.IntegerField()

class Client(models.Model):
    code = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    rtn = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class Transaction_x_Invoice(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)

class Detail(models.Model):
    unit_price = models.IntegerField()
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

class ISV(models.Model):
    numeric_percent = models.IntegerField()
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)
    isv_type = models.ForeignKey(ISV_Type, on_delete=models.CASCADE)

class Discount(models.Model):
    numeric_percent = models.IntegerField()
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)
    discount_type = models.ForeignKey(Discount_Type, on_delete=models.CASCADE)

    







