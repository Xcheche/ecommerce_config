from django.shortcuts import render

from store.models import Category


# Create your views here.
def store(request):
    return render(request, 'store/store.html')


# Category

def category(request):
    all_category = Category.objects.all()
    return {'all_category': all_category}