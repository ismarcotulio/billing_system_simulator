from django.contrib import admin
from .models import ISV_Type, Discount_Type, Product, Invoice, Transaction, Client, Transaction_x_Invoice, Detail, ISV, Discount

# Register your models here.
admin.site.register(ISV_Type)
admin.site.register(Discount_Type)
admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(Transaction)
admin.site.register(Client)
admin.site.register(Transaction_x_Invoice)
admin.site.register(Detail)
admin.site.register(ISV)
admin.site.register(Discount)
