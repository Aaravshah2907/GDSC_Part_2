# order_management_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/<int:order_id>/update/',
         views.order_update, name='order_update'),
    path('orders/<int:order_id>/delete/',
         views.order_delete, name='order_delete'),
]
