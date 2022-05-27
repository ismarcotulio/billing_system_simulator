from rest_framework import serializers
from todo.models import Todo

from billing.models import ISV_Type, Discount_Type, Product, Invoice, Transaction, Client, Transaction_x_Invoice, Detail, ISV, Discount

class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'created', 'completed']

class TodoToggleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id']
        read_only_fields = ['title', 'memo', 'created', 'completed']

class ISV_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ISV_Type
        fields = ['id', 'name', 'description']

class Discount_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount_Type
        fields = ['id', 'name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'code', 'name', 'description', 'suggested_public_price']

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'cai', 'datetime_issue']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'reduction']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'code', 'first_name', 'last_name', 'phone', 'rtn', 'email']

class Transaction_X_InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction_x_Invoice
        fields = ['id', 'invoice', 'client', 'employee']

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ['id', 'unit_price', 'quantity', 'product', 'transaction']

class ISVSerializer(serializers.ModelSerializer):
    class Meta:
        model = ISV
        fields = ['id', 'numeric_percent', 'detail', 'isv_type']

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'numeric_percent', 'detail', 'discount_type']
