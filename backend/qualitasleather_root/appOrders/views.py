from django.shortcuts import render
from django.http import HttpResponse

from .models import Order
from appProductItem.models import ProductItem
# Create your views here.


def makeorder(request):
    print('!!!!!!!!!!!!!!!!!!!!!!!')
    newOrder = Order()
    newOrder.order_binding = ProductItem.objects.get(pk=request.POST['product-id'])
    newOrder.order_customer_name = request.POST['customer-name']
    newOrder.order_customer_telephone = request.POST['customer-telephone']
    newOrder.order_customer_comment = request.POST['customer-commet']
    newOrder.save()
    return HttpResponse("True")