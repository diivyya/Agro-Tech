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

def predict(request):
    data = []
    data.append(request.POST.get('tempVal'))
    data.append(request.POST.get('humidityVal'))
    data.append(request.POST.get('phVal'))
    data.append(request.POST.get('rainfallVal'))

    md = joblib.load('final_model.sav')
    predictcrop=[data]
    # Putting the names of crop in a single list
    crops=['wheat','mungbean','Tea','millet','maize','lentil','jute','cofee','cotton','ground nut','peas','rubber','sugarcane','tobacco','kidney beans','moth beans','coconut','blackgram','adzuki beans','pigeon peas','chick peas','banana','grapes','apple','mango','muskmelon','orange','papaya','watermelon','pomegranate']
    cr='rice'
    predictions = md.predict(predictcrop)
    count=0
    for i in range(0,30):
        if(predictions[0][i]==1):
            c=crops[i]
            count=count+1
            break
        i=i+1
    if(count==0):
        context = {'ans': cr}
    else:
        context = {'ans': c}
    return render(request,'crop_pred.html',context)



