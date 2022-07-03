from django.shortcuts import render
from appProductCategory.views import getProductsCategorys, getProductsCategorysById
from appProductItem.views import getProdItemsByCategory, getProdItemById, getProdImagesById, getProdItemInCategorys
# Create your views here.

# Получаем список категорий товаров из базы данных для главного меню.
productCategoryList = getProductsCategorys()

# Функции вызываемые после обработки route, в зависимости от адреса
def index_page(request):
    prodItemsInGroups = getProdItemInCategorys()
    print(prodItemsInGroups)
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
    # Отрисовываем полученные данные на странице
    return render(request, './product.html', {
        'productCategoryList' : productCategoryList,
        'prodItem' : prodItem,
        'prodImages' : prodImages,
    })

def contacts_page(request):
    # Отрисовываем полученные данные на странице
    return render(request, './contacts.html', {
        'productCategoryList' : productCategoryList
    })
