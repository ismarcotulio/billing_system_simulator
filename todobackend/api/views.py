from rest_framework import generics, permissions
from .serializers import TodoSerializer, TodoToggleCompleteSerializer, ISV_TypeSerializer, Discount_TypeSerializer, ProductSerializer, InvoiceSerializer
from todo.models import Todo
from billing.models import ISV_Type, Discount_Type, Product, Invoice
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

## OBJECT LIST VIEWS -----------------------------------------------------------------------

class TodoList(generics.ListAPIView):
    # ListAPIView requires two mandatory attributes, serializer_class and queryset.
    # We specify TodoSerializer which we have earier implemented
    serializer_class = TodoSerializer

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by('-created')

class ISV_TypeList(generics.ListAPIView):
    serializer_class = ISV_TypeSerializer

    def get_queryset(self):
        return ISV_Type.objects.all()

class Discount_TypeList(generics.ListAPIView):
    serializer_class = Discount_TypeSerializer

    def get_queryset(self):
        return Discount_Type.objects.all()

class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

class InvoiceList(generics.ListAPIView):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        return Invoice.objects.all()



## OBJECT LIST CREATE VIEWS -----------------------------------------------------------------------

class TodoListCreate(generics.ListCreateAPIView):
    # ListAPIView requires two mandatory attributes, serializer_class and queryset.
    # We specify TodoSerializer which we have earlier implemented.
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by('-created')

    def perform_create(self, serializer):
        # serializer holds a django model
        serializer.save(user=self.request.user)

class ProductListCreate(generics.ListCreateAPIView):
    # ListAPIView requires two mandatory attributes, serializer_class and queryset.
    # We specify TodoSerializer which we have earlier implemented.
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Product.objects.all()
        
    def perform_create(self, serializer):
        # serializer holds a django model
        serializer.save()


class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # user can only update, delete own posts
        return Todo.objects.filter(user=user)

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.all()

class TodoToggleComplete(generics.UpdateAPIView):
    serializer_class = TodoToggleCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.instance.completed = not(serializer.instance.completed)
        serializer.save()

@csrf_exempt
def signup(request):
    if request.method == "POST":
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(
                username = data['username'],
                password = data['password']
            )
            user.save()

            token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=201)
        except IntegrityError:
            return JsonResponse(
                {'error':'username taken, chose another username'}, status=400
            )

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
            request,
            username=data['username'],
            password=data['password']
        )
        if user is None:
            return JsonResponse(
                {'error':'unable to login, check username and password'},
                status = 400
            )
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=201)
