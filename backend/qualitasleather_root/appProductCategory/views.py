from django.shortcuts import render
from .models import ProductCategory

# Create your views here.

def getProductsCategorys():
    # Получаем данные из БД
    slider_list = ProductCategory.objects.all()
    return slider_list