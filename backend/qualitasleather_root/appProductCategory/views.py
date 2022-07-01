from django.shortcuts import render
from .models import ProductCategory

# Create your views here.

def getProductsCategorys():
    # Получаем данные из БД
    group_list = ProductCategory.objects.all()
    return group_list

def getProductsCategorysById(idProductCategory):
    # Получаем данные из БД
    group_list = ProductCategory.objects.all()
    for group in group_list:
        if (group.id == idProductCategory):
            return group