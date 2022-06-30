from django.db import models

# Create your models here.

# Формирование модели приложения "Категория товара" (сумки, кошельки и тд)
class ProductCategory(models.Model):
    # product_category_name - имя поля таблицы с типом CharField
    # max_length - максимальное количество симоволо
    # verbose_name - имя поля отображаемого в админ панеле
    product_category_name = models.CharField(max_length=200, verbose_name='Категория товара')

    # Измененеие отображения имени объекта. __str__ - это строковое представление объекта
    # Получим корректное отображение имени объекта в админ паненле
    def __str__(self):
        return self.product_category_name

    # Изменение отображения имени класса, в единственном и множественном числе
    class Meta:
        verbose_name = "Категория товара"
        verbose_name_plural = "Категории товаров"