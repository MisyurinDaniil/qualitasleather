from django.db import models

# Create your models here.

class ProductGroup(models.Model):
    # product_group_name - имя поля таблицы с типом CharField
    # max_length - максимальное количество симоволо
    # verbose_name - имя поля отображаемого в админ панеле
    product_group_name = models.CharField(max_length=200, verbose_name='Группа товара')

    # Измененеие отображения имени объекта. __str__ - это строковое представление объекта
    # Получим корректное отображение имени объекта в админ паненле
    def __str__(self):
        return self.product_group_name

    # Изменение отображения имени класса, в единственном и множественном числе
    class Meta:
        verbose_name = "Группа товара"
        verbose_name_plural = "Группы товаров"