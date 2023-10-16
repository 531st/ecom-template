from django.shortcuts import render



def store(request):
    context = {}
    return render(request, 'shopApp/store.html', context)


def cart(request):
    context = {}
    return render(request, 'shopApp/cart.html', context)


def checkout(request):
    context = {}
    return render (request, 'shopApp/checkout.html', context)