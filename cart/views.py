from django.shortcuts import render

# Create your views here.

def cart_summary(request):
    return render(request,"cart/cart_summary.html")


def cart_add(request):
    return render(request,"cart/cart_add.html")


def cart_update(request):
    return render(request,"cart/cart_update.html")


def cart_delete(request):
    return render(request,"cart/cart_delete.html")