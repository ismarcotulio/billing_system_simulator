from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.TodoListCreate.as_view()),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete', views.TodoToggleComplete.as_view()),
    path('signup/', views.signup),
    path('login/', views.login),

    path('isv_type/', views.ISV_TypeList.as_view()),

    path('discount_type/', views.Discount_TypeList.as_view()),

    path('product/', views.ProductListCreate.as_view()),
    path('product/<int:pk>', views.ProductRetrieveUpdateDestroy.as_view()),

    path('invoice/', views.InvoiceList.as_view())
]