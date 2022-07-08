from django.shortcuts import render
from django.http import HttpResponse

from appProductCategory.views import getProductsCategorys, getProductsCategorysById
from appProductItem.views import getProdItemsByCategory, getProdItemById, getProdImagesById, getProdItemInGroups
# Create your views here.

# Получаем список категорий товаров из базы данных для главного меню.
productCategoryList = getProductsCategorys()

# Функции вызываемые после обработки route, в зависимости от адреса
def index_page(request):
    # Получаем товары товары в соответствующих категориях
    prodItemsInGroups = getProdItemInGroups()
    # Отрисовываем полученные данные на странице
    return render(request, './index.html', {
        'productCategoryList' : productCategoryList,
        'prodItemsInGroups' : prodItemsInGroups,
    })

def category_page(request, idProductCategory):
    # Получаем список товаров определенной категории по ID категории
    prodItemsByCategory = getProdItemsByCategory(idProductCategory)
    # Получаем категорию товара по id категории, для вывода в заголовок
    prodCategory = getProductsCategorysById(idProductCategory)
    # Отрисовываем полученные данные на странице 
    return render(request, './category.html', {
        'productCategoryList' : productCategoryList,
        'prodItemsByCategory' : prodItemsByCategory,
        'prodCategory' : prodCategory,
    })

def product_page(request, idProductItem):
    # Получаем товар по ID товара 
    prodItem = getProdItemById(idProductItem)
    # Получаем картинки товараов по ID товара 
    prodImages = getProdImagesById(idProductItem)
    # Получаем абсолютный URL (http://127.0.0.1:8000/product/2/)
    productURL = request.build_absolute_uri()
    # Отрисовываем полученные данные на странице
    return render(request, './product.html', {
        'productCategoryList' : productCategoryList,
        'prodItem' : prodItem,
        'prodImages' : prodImages,
        'productURL': productURL,
    })

def contacts_page(request):
    # Отрисовываем полученные данные на странице
    return render(request, './contacts.html', {
        'productCategoryList' : productCategoryList
    })

