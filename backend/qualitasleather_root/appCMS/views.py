from django.shortcuts import render
from appProductCategory.views import getProductsCategorys
from appProductItem.views import getProductsItems 
# Create your views here.


# Получаем список категорий товаров
productCategoryList = getProductsCategorys()
# Функции вызываемы после обработки route, в зависимости от адреса
def index_page(request):

    # Отрисовываем полученные данные на странице
    return render(request, './index.html', {
        'productCategoryList' : productCategoryList
    })

def category_page(request, idProductCategory):
    # Отрисовываем полученные данные на странице 
    return render(request, './category.html', {
        'productCategoryList' : productCategoryList
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
