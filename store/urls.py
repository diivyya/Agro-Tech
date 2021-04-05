from django.contrib import admin
from django.urls import path
from .views import etrade, index, crop_pred, predict

urlpatterns = [
    path('',index,name='homepage'),
    path('etrade',etrade, name='etradpage'),
    path('crop_prediction',crop_pred,name='croppredpage'),
    path('predict',predict, name='predict'),
]
