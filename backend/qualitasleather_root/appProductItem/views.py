from django.shortcuts import render
from .models import ProductItem, ProductImg

# Create your views here.

# def getProdItemsByCategory(productCategoryId):
def getProdItemsByCategory(idProductCategory):
    products = ProductItem.objects.all()
    filterProducts = []
    for product in products:
        if (product.__dict__['product_category_id'] == idProductCategory):
            filterProducts.append(product)
            
    return filterProducts

def getProdItemById(idProductItem):
    # Invalid field name(s) given in select_related: 'productmaketime_set'. Choices are: product_category, product_group, product_color, product_material, product_fitting, product_make_time
    product = ProductItem.objects.select_related('product_color', 'product_material', 'product_fitting', 'product_make_time').get(id=idProductItem)
    return product

def getProdImagesById(idProductItem):
    images = ProductImg.objects.filter(img_binding=idProductItem)
    return images

def getProdItemInCategorys():
    products = ProductItem.objects.select_related('product_category').exclude(product_group=1)
    return products
