from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
import joblib

# Create your views here.

def etrade(request):
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
    return render(request,'etrade.html',data)

def index(request):
    return render(request,'index.html')


def crop_pred(request):
    return render(request,'crop_pred.html')

def result(request):

    md = joblib.load('final_model.sav')

    lis = []
    lis.append(request.GET.get('temperature'))
    lis.append(request.GET.get('humidity'))
    lis.append(request.GET.get('ph'))
    lis.append(request.GET.get('rainfall'))

    ans = md.predict([lis])
    return render(request,'result.html',ans)