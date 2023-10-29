# order_management_app/views.py
from django.shortcuts import render, redirect
from .models import Order
from fuzzywuzzy import fuzz
from django.http import Http404


def order_list(request):
    orders = Order.objects.filter(creator=request.user)
    return render(request, 'order_list.html', {'orders': orders})


def order_create(request):
    if request.method == 'POST':
        description = request.POST['description']
        priority = request.POST['priority']
        Order.objects.create(creator=request.user,
                             description=description, priority=priority)
        return redirect('order_list')
    return render(request, 'order_form.html')


def order_update(request, order_id):
    order = Order.objects.get(id=order_id)
    if order.creator != request.user:
        raise Http404("You don't have permission to edit this order.")
    if request.method == 'POST':
        order.description = request.POST['description']
        order.priority = request.POST['priority']
        order.save()
        return redirect('order_list')
    return render(request, 'order_form.html', {'order': order})


def order_delete(request, order_id):
    order = Order.objects.get(id=order_id)
    if order.creator != request.user:
        raise Http404("You don't have permission to delete this order.")
    order.delete()
    return redirect('order_list')
