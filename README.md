История КОММИТОВ:

### 15\. 22:47 15.07.2022 г.
    Добавил forms.py к приложению appOrders (используем django forms)

### 14\. 00:22 09.07.2022 г.
    Добавил оповещение в telegram

### 13\. 15:21 08.07.2022 г.
    Добавил favico

### 12\. 15:21 08.07.2022 г.
    Сделал отправку формы заказа (JS - fetch API AJAX) и обработку ее 
    на сервере (сделал приложенеи appOrders -> model, view) с записью в БД

### 11\. 15:21 03.07.2022 г.
    Случайно удалил предыдущий коммит. Сгорел, не смог восстановить.
    Переписал все зановов.
    Сделал вывод товаров по группам на главной странице. 
    Переименованы названия приложений в панели администратора
    Разобрался и настроил .gitignore

### 10\. 12:28 03.07.2022 г.
    Сделал вывод товаров по группам на главной странице. 
    Переименованы названия приложений в панели администратора
    Разобрался и настроил .gitignore

### 9\. 15:28 02.07.2022 г.
    Закончил конечную страницу товара (вывод информации о товаре из БД).

### 8\. 19:51 01.07.2022 г.
    Написал вывод товаров определеннй категории на страницу категории товара (category.html)
    по нажатию ссылки в главном меню.
    Начал писать вывод данных из БД на страницу товара (шаблон product.html).
    Выгрузил список использемых в проекте python пакетов (requirements.txt).

### 7\. 12:05 30.06.2022 г.
    Изменил README.md файл

### 6\. 12:03 30.06.2022 г.
    Изменил README.md файл

### 5\. 12:00 30.06.2022 г.
    Изменил README.md файл

### 4\. 11:28 30.06.2022 г.
    Создал приложения:
    appCMS - через view данного app плучаем все данные и отдаем шаблонам;
    appIndexSlider - app для банера конрневого шаблона base.html;
    appProductCategory - app для работы с категориями товаров (сумки, чехлы);
    appProductGroup - app для работы с группами товаров (sale, popular, new);
    appProductItem - app для работы с экземпляром товара.
    Создал модели вышеперечисленных приложений. Произвел миграцию.
    Добавил в админ панель и настроил вышеперечисленные приложения.
    Обработал фото для 3х уникальных товаров.
    Поправил .gitignore

### 3\.  15:26 28.06.2022 г.
    Разбил все страницы на шаблоны. Выполнил подключение и наследоване шаблонов.
    Подключил все статические файлы.

### 2\.  17:09 27.06.2022 г. 
    Обновил слайдер до версии fancybox v.4. 
    Изменил структуту html блоков слайдера на странице товара (стайрый слайдер со 
    всей структурой блоков удален).
    
### 1\.  11:39 26.06.2022 г. 
    Разделил проект на Frontend и Backend части (директории). Frontend закончен. 
    Слайдер на странице продукта в начале процесса переработки. 