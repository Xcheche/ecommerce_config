from django.shortcuts import render
from django.shortcuts import get_object_or_404

from store.models import Category, Product


# Create your views here.
def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)


# Product Detail using only the slug
def product_info(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, 'store/product_info.html', context)



# Category

def category(request):
    all_category = Category.objects.all()
    return {'all_category': all_category}


# List Category
def list_category(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {'category': category, 'products': products}
    return render(request, 'store/list_category.html', context)