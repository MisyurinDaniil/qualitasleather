# импортируем класс forms
from django import forms

class OrderForm(forms.Form):
    # Создаем два поля класса OrderForm
    # Создаем два input type=text, все поля являеютмя обязательными для заполнения поумолчанию,
    # форма не отправится без заполненных полей, имеет встроенную валидацию
    # required=False - делает поле необязательным
    # widget=forms.TextInput(attrs={'class' : 'css-input'} - зададим класс тегу input для настройки css
    customer_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class' : 'modal-window__input',
        'placeholder' : 'Имя',
        'id' : 'input-name',
        }))
    customer_telephone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class' : 'modal-window__input',
        'placeholder' : 'Номер телефона',
        'id' : 'input-telephone',
        }))
    customer_commet = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
        'class' : 'modal-window__input',
        'placeholder' : 'Комментарий',
        'id' : 'input-commet',
        }))