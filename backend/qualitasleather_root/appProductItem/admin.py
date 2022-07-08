from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import ProductItem, ProductColor, ProductMaterial, ProductFitting, ProductMakeTime, ProductImg

# Register your models here.
class ShowImagesInProduct(admin.StackedInline):
    # Указываем обязательный атрибут - модель к которой относится данный класс
    model = ProductImg
    # Указжем поля отображаемые на карточке слайда
    fields = ('img_small', 'get_img_small', 'alt_small', 'img_medium', 'get_img_medium', 
        'alt_medium', 'img_big', 'get_img_big', 'alt_big')
    # Укажем поля только для чтения, чтобы django не вывалилвался в ошибку
    readonly_fields = ('get_img_small', 'get_img_medium', 'get_img_big')
    # Функция для отображения миниатюры картинки в админ панеле
    def get_img_small(self, obj):
        if obj.img_small:
            return mark_safe(f'<img src="{obj.img_small.url}" width="80px"')
        else:
            return 'нет картинки'
    def get_img_medium(self, obj):
        if obj.img_medium:
            return mark_safe(f'<img src="{obj.img_medium.url}" width="80px"')
        else:
            return 'нет картинки'
    def get_img_big(self, obj):
        if obj.img_big:
            return mark_safe(f'<img src="{obj.img_big.url}" width="80px"')
        else:
            return 'нет картинки'
    # Строковое представление функции get_img
    get_img_small.short_description = 'Миниатюра 100х100'
    get_img_medium.short_description = 'Миниатюра 330х330'
    get_img_big.short_description = 'Миниатюра большая'



    # Задаим одно поле ввода для модели Comment = 1, если указать 0 - необходимо нажимать зеленый плюс
    # для отображения поля комментария
    extra = 0

class CustomizeProductItem(admin.ModelAdmin):
    # Кортеж с именами полей, который хотим отобразит в админ панеле на этапе просмотра всего перечня товаров
    list_display = ('id', 'product_name', 'get_img')
    # Отмечаем поля по нажатию на которые можно перейти на страницу слайда
    list_display_links = ('id', 'product_name', 'get_img')
    # Указжем поля отображаемые на карточке слайда
    fields = ('product_name', 'product_category', 'product_group', 'product_price', 'product_old_price',
        'product_color', 'product_material', 'product_fitting', 'product_make_time', 'product_size', 
        'product_description', 'product_img_main', 'get_img', 'product_img_main_alt')
    # Укажем поля только для чтения, чтобы django не вывалилвался в ошибку
    readonly_fields = ('get_img', )
    # Укажем сколько строк на одной странице
    list_per_page = 10
    # Укажем максимальное количество полей при выводе всех
    list_max_show_all = 100
    # Передадим класс ProductImages для отображения полей добавления картинок на странице добавления товара
    # По умолчанию одается 3 поля сторонней модели
    inlines = [ShowImagesInProduct,]
    # Функция для отображения миниатюры картинки в админ панеле
    def get_img(self, obj):
        if obj.product_img_main:
            return mark_safe(f'<img src="{obj.product_img_main.url}" width="80px"')
        else:
            return 'нет картинки'
    # Строковое представление функции get_img
    get_img.short_description = 'Миниатюра 250х235'

class CustomizeProductImg(admin.ModelAdmin):
    # Кортеж с именами полей, который хотим отобразит в админ панеле на этапе просмотра всего перечня картинок
    list_display = ('id', 'get_img_small')
    # Отмечаем поля по нажатию на которые можно перейти на страницу слайда
    list_display_links = ('id', 'get_img_small')
    # Указжем поля отображаемые на карточке слайда
    fields = ('img_binding', 'img_small', 'get_img_small', 'alt_small', 'img_medium', 'get_img_medium', 
        'alt_medium', 'img_big', 'get_img_big', 'alt_big')
    # Укажем поля только для чтения, чтобы django не вывалилвался в ошибку
    readonly_fields = ('get_img_small', 'get_img_medium', 'get_img_big')
    # Функция для отображения миниатюры картинки в админ панеле
    def get_img_small(self, obj):
        if obj.img_small:
            return mark_safe(f'<img src="{obj.img_small.url}" width="80px" height="50px"')
        else:
            return 'нет картинки'
    def get_img_medium(self, obj):
        if obj.img_medium:
            return mark_safe(f'<img src="{obj.img_medium.url}" width="80px"')
        else:
            return 'нет картинки'
    def get_img_big(self, obj):
        if obj.img_big:
            return mark_safe(f'<img src="{obj.img_big.url}" width="80px"')
        else:
            return 'нет картинки'
    # Строковое представление функции get_img
    get_img_small.short_description = 'Миниатюра'
    get_img_medium.short_description = 'Миниатюра'
    get_img_big.short_description = 'Миниатюра'

# Добавляем нашу модель в админ панель
admin.site.register(ProductItem, CustomizeProductItem)
admin.site.register(ProductColor)
admin.site.register(ProductMaterial)
admin.site.register(ProductFitting)
admin.site.register(ProductMakeTime)
admin.site.register(ProductImg, CustomizeProductImg)