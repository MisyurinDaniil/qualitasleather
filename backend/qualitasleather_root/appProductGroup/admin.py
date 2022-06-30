from django.contrib import admin
from .models import ProductGroup

# Register your models here.

# Настраиваем отображение в админ панеле
class CustomizeProductGroup(admin.ModelAdmin):
    # Кортеж с именами полей, который хотим отобразит в админ панеле на этапе просмотра слайдов
    list_display = ('id', 'product_group_name')
    # Определяем поля, которые можно отредактировать, не переходя на отдельный слайд
    list_editable = ('product_group_name', )
    # Укажем поля только для чтения, чтобы django не вывалилвался в ошибку
    readonly_fields = ('id', )

# Добавляем нашу модель в админ панель
admin.site.register(ProductGroup, CustomizeProductGroup)