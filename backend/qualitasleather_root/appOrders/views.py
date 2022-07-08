from django.shortcuts import render
from django.http import HttpResponse

from .models import Order
from appProductItem.models import ProductItem
from appTelegram.sendmessage import sendTelegram
# Create your views here.


def makeorder(request):
    newOrder = Order()

    product_id = request.POST['product-id']
    customer_name = request.POST['customer-name']
    customer_telephone = request.POST['customer-telephone']
    customer_commet = request.POST['customer-commet']
    product_name = ProductItem.objects.get(pk=product_id).product_name
    server_url = request.get_host()
    get_full_path = request.POST['get-full-path']

    text = ('ID товара - ' + product_id + '\n' + 
            'Ссылка на товар - ' + server_url + get_full_path + '\n' + 
            'Название товара - ' + product_name + '\n' + 
            'Имя заказчика - ' + customer_name + '\n' + 
            'Телефон закачика - ' + customer_telephone + '\n' + 
            'Комментарий к заказу - ' + customer_commet)

    newOrder.order_binding = ProductItem.objects.get(pk=product_id)
    newOrder.order_customer_name = customer_name
    newOrder.order_customer_telephone = customer_telephone
    newOrder.order_customer_comment = customer_commet
    newOrder.save()

    sendTelegram(text)

    return HttpResponse("True")