# Generated by Django 4.0.5 on 2022-07-08 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProductItem', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcolor',
            options={'verbose_name': 'Цвет', 'verbose_name_plural': '3. Цвета'},
        ),
        migrations.AlterModelOptions(
            name='productfitting',
            options={'verbose_name': 'Фурнитура', 'verbose_name_plural': '5. Фурнитруа'},
        ),
        migrations.AlterModelOptions(
            name='productimg',
            options={'verbose_name': 'Картинка для слайдера товара', 'verbose_name_plural': '2. Картинки для сладера товара'},
        ),
        migrations.AlterModelOptions(
            name='productitem',
            options={'verbose_name': 'Товар', 'verbose_name_plural': '1. Товары'},
        ),
        migrations.AlterModelOptions(
            name='productmaketime',
            options={'verbose_name': 'Время изготовления', 'verbose_name_plural': '6. Время изготовления'},
        ),
        migrations.AlterModelOptions(
            name='productmaterial',
            options={'verbose_name': 'Материал', 'verbose_name_plural': '4. Материалы'},
        ),
        migrations.AlterField(
            model_name='productimg',
            name='alt_big',
            field=models.CharField(max_length=200, verbose_name='Альтернативный текст большой картинки'),
        ),
        migrations.AlterField(
            model_name='productimg',
            name='alt_medium',
            field=models.CharField(max_length=200, verbose_name='Альтернативный текст средней картинки'),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='product_img_main',
            field=models.ImageField(upload_to='product_img/', verbose_name='Картинка для группы товаров 250х235'),
        ),
    ]