from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
# Create your views here.

def index(request):
    products = Product.get_all_products()
    categories = Category.get_all_categories()
    category_id = request.GET.get('category')
    if category_id:
        products = Product.get_all_products_by_category_id(category_id)
    else:
        products = Product.get_all_products()
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request,'index.html',data)

def home(request):
    return render(request,'home.html')


def crop_pred(request):
    return render(request,'crop_pred.html')