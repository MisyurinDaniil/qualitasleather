from django.shortcuts import render

# Create your views here.


def index_page(request):
    # Отрисовываем полученные данные на странице index.html
    return render(request, './index.html')

def category_page(request):
    # Отрисовываем полученные данные на странице index.html
    return render(request, './category.html')

def product_page(request):
    # Отрисовываем полученные данные на странице index.html
    return render(request, './product.html')

def contacts_page(request):
    # Отрисовываем полученные данные на странице index.html
    return render(request, './contacts.html')
