from django.shortcuts import render
from appProductCategory.views import getProductsCategorys, getProductsCategorysById
from appProductItem.views import getProdItemsByCategory
# Create your views here.

# Получаем список категорий товаров из базы данных для главного меню.
productCategoryList = getProductsCategorys()

# Функции вызываемые после обработки route, в зависимости от адреса
def index_page(request):
    # Отрисовываем полученные данные на странице
    return render(request, './index.html', {
        'productCategoryList' : productCategoryList
    })

def category_page(request, idProductCategory):
    # Получаем товары определенной категории по ее ID
    prodItemsByCategory = getProdItemsByCategory(idProductCategory)
    # Получаем категорию товара по ее id, для вывода в заголовок
    prodCategory = getProductsCategorysById(idProductCategory)
    # Отрисовываем полученные данные на странице 
    return render(request, './category.html', {
        'productCategoryList' : productCategoryList,
        'prodItemsByCategory' : prodItemsByCategory,
        'prodCategory' : prodCategory,
    })

def product_page(request):
    # Отрисовываем полученные данные на странице
    return render(request, './product.html', {
        'productCategoryList' : productCategoryList
    })

def contacts_page(request):
    # Отрисовываем полученные данные на странице
    return render(request, './contacts.html', {
        'productCategoryList' : productCategoryList
    })
