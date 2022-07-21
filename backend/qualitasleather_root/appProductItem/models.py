from django.db import models
from appProductCategory.models import ProductCategory
from appProductGroup.models import ProductGroup

# Create your models here.
# Создаем класс (модел) для таблицы цвета
class ProductColor(models.Model):
    # color - имя поля таблицы с типом CharField
    # max_length - максимальное количество симоволо
    # verbose_name - имя поля отображаемого в админ панеле
    color = models.CharField(max_length=255, verbose_name='Цвет')

    # Измененеие отображения имени объекта. __str__ - это строковое представление объекта
    # Получим корректное отображение имени объекта в админ паненле
    def __str__(self):
        return self.color

    # Изменение отображения имени класса, в единственном и множественном числе
    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "3. Цвета"

# Создаем класс (модел) для таблицы Материалы
class ProductMaterial(models.Model):
    material = models.CharField(max_length=255, verbose_name='Материал')

    def __str__(self):
        return self.material

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "4. Материалы"

# Создаем класс (модел) для таблицы Фурнитура
class ProductFitting(models.Model):
    fitting = models.CharField(max_length=255, verbose_name='Фурнитура')

    def __str__(self):
        return self.fitting

    class Meta:
        verbose_name = "Фурнитура"
        verbose_name_plural = "5. Фурнитруа"  

# Создаем класс (модел) для таблицы Время изготовления
class ProductMakeTime(models.Model):
    make_time = models.CharField(max_length=255, verbose_name='Время изготовления')

    def __str__(self):
        return self.make_time

    class Meta:
        verbose_name = "Время изготовления"
        verbose_name_plural = "6. Время изготовления"  

# Создаем класс (модел) для таблицы Товар
class ProductItem(models.Model):
    product_name = models.CharField(max_length=255, verbose_name='Наименование')
    product_category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, verbose_name='Категория товара')
    product_group = models.ForeignKey(ProductGroup, on_delete=models.PROTECT, verbose_name='Группа товара')
    product_price = models.CharField(max_length=255, verbose_name='Цена')
    product_old_price = models.CharField(max_length=255, default='-',  verbose_name='Старая цена')
    product_color = models.ForeignKey(ProductColor, on_delete=models.PROTECT, verbose_name='Цвет')
    product_material = models.ForeignKey(ProductMaterial, on_delete=models.PROTECT, verbose_name='Материал')
    # Связываем таблицы через тип поля ForeignKey, вторым параметром указывается что делать при
    # удалении поля (on_delete=models.PROTECT - запрещает удалять поля при удалении родителя)
    # blank - для пустоты в админ панели django
    product_fitting = models.ForeignKey(ProductFitting, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Фурнитура')
    product_make_time = models.ForeignKey(ProductMakeTime, on_delete=models.PROTECT, verbose_name='Время изготовления')
    product_size = models.CharField(max_length=255, verbose_name='Размер')
    product_description = models.TextField(verbose_name='Описание')
    product_img_main = models.ImageField(upload_to='product_img/', verbose_name='Картинка для группы товаров 250х235')
    product_img_main_alt = models.CharField(max_length=255, verbose_name='Альтернативный текст фото')

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "1. Товары"

# Создаем класс (модел) для таблицы Картинки товара
class ProductImg(models.Model):
    # Связываем таблицы через тип поля ForeignKey
    # on_delete=models.CASCADE - при удалении родителя (товара) удалиться связанная с ним таблица (картинки)
    img_binding = models.ForeignKey(ProductItem, on_delete=models.CASCADE, verbose_name='Товар')
    img_small = models.ImageField(upload_to='product_img/', verbose_name='Маленькая картинка 96х64')
    alt_small = models.CharField(max_length=200, verbose_name='Альтернативный текст маленькой картинки')
    img_medium = models.ImageField(upload_to='product_img/', verbose_name='Средняя картинка 330х330')
    alt_medium = models.CharField(max_length=200, verbose_name='Альтернативный текст средней картинки')
    img_big = models.ImageField(upload_to='product_img/', verbose_name='Большая картинка 1680х945')
    alt_big = models.CharField(max_length=200, verbose_name='Альтернативный текст большой картинки')

    def __str__(self):
        return self.alt_small

    class Meta:
        verbose_name = "Картинка для слайдера товара"
        verbose_name_plural = "2. Картинки для сладера товара"