from django.contrib import admin
from .models.product import Product
from .models.category import Category
# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','phoneno','category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)