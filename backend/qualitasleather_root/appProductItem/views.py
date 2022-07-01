from django.shortcuts import render
from .models import ProductItem

# Create your views here.

# def getProdItemsByCategory(productCategoryId):
def getProdItemsByCategory(idProductCategory):
    product_list = ProductItem.objects.all()
    filterProducts = []
    for product in product_list:
        if (product.__dict__['product_category_id'] == idProductCategory):
            filterProducts.append(product)
            
    return filterProducts

# print(getProdItemsByCategory())

# {'_state': <django.db.models.base.ModelState object at 0x000001AA6981BEB0>, 'id': 1, 
# 'product_name': 'Сумка черная большая', 'product_category_id': 1, 'product_group_id': 1, 
# 'product_price': '17880', 'product_old_price': '20120', 'product_color_id': 1, 
# 'product_material_id': 1, 'product_fitting_id': 1, 'product_make_time_id': 1, 
# 'product_size': '17х19х20', 'product_description': 'Самый волшебный сумка, которую ты видел, БРАТ!',
#  'product_img_main': 'product_img/black-bag-250x235-001.jpg', 'product_img_main_alt': 'картинка'}