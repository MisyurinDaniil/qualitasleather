from django.shortcuts import render
from .models import ProductItem

# Create your views here.

def getProductsItems():
    # Получаем данные из БД
    product_list = ProductItem.objects.all()
    print(product_list, type(product_list))
    # >>> <QuerySet [<ProductItem: Сумка черная большая>]> <class 'django.db.models.query.QuerySet'>

getProductsItems()


# Разбриаемся с Python. Типы данных, переменные

number = 1
print(number, type(number))
# >>> 1 <class 'int'>

text = 'My text'
print(text, type(text))
# >>> My text <class 'str'>

type_list = [1, 'a', 2, 'b', [1, 'a', 2, 'b'], (1, 'a', 2, 'b')]
print(type_list, type(type_list))
# >>> [1, 'a', 2, 'b'] <class 'list'>

corteg=(1, 'a', 2, 'b')
print(corteg, type(corteg))
# >>> (1, 'a', 2, 'b') <class 'tuple'>

dictionary = {
    '1': 1,
    2 : 2,
    'Три' : 'Три'
}
print(dictionary, type(dictionary))

class MyClass():
    def __init__(self, name, age):
        self.name = name
        self.age = age
people = MyClass('Pol','11')
print(MyClass, type(MyClass))
print(people, type(people))
# >>> <class 'appProductItem.views.MyClass'> <class 'type'>
# >>> <appProductItem.views.MyClass object at 0x00000172EE585D20> <class 'appProductItem.views.MyClass'>