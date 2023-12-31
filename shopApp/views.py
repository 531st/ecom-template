from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json



def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.cart_items
    else:
        items = []
        order = { 'cart_total': 0, 'cart_items': 0, 'shipping': False}
        cartItems = order['cart_items']

    products = Product.objects.all()
    context = {
        'products': products,
        'cartItems': cartItems,
    }
    return render(request, 'shopApp/store.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.cart_items
    else:
        items = []
        order = { 'cart_total': 0, 'cart_items': 0, 'shipping': False}
        cartItems = order['cart_items']

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }
    return render(request, 'shopApp/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.cart_items
    else:
        items = []
        order = { 'cart_total': 0, 'cart_items': 0, 'shipping': False}
        cartItems = order['cart_items']

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }
    return render (request, 'shopApp/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('Item was updated', safe=False)