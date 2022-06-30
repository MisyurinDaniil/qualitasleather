from django.contrib import admin
from .models import ProductCategory

# Register your models here.

# Настраиваем отображение в админ панеле
class CustomProductCategory(admin.ModelAdmin):
    # Кортеж с именами полей, который хотим отобразит в админ панеле на этапе просмотра слайдов
    list_display = ('id', 'product_category_name')
    # Определяем поля, которые можно отредактировать, не переходя на отдельный слайд
    list_editable = ('product_category_name', )
    # Укажем поля только для чтения, чтобы django не вывалилвался в ошибку
    readonly_fields = ('id', )

# Добавляем нашу модель в админ панель
admin.site.register(ProductCategory, CustomProductCategory)