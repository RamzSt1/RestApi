from django.shortcuts import render, redirect
import requests

# Create your views here.
from galacticexpress.apps import template
from galacticexpress.models import News


def index(request):
    context = {}
    news = News.objects.all()
    context.update({'news': news})
    #
    # response_type = requests.get('http://127.0.0.1:8000/api/jewelry_type/')
    # if response_type.headers['Content-Type'] == 'application/json':
    #     context.update({"jewelry_type": response_type.json()})

    return render(request, template + '/index.html', context=context)

def orders(request):
    context = {}

    response_type = requests.get('http://127.0.0.1:8000/customer/api/orders/')
    if response_type.headers['Content-Type'] == 'application/json':
        orders = []
        for i in response_type.json():
            if i['client'] == request.user.id:
                orders.append(i)

        context.update({'orders': orders})
    return render(request, template + '/orders.html', context=context)

def new_order(request):
    context = {}
    response_type = requests.get('http://127.0.0.1:8000/customer/api/gabarits/')
    if response_type.headers['Content-Type'] == 'application/json':
        context.update({'gabarits': response_type.json()})

    print(request.POST)
    if request.POST:
        client = request.user.id
        fio = request.POST.get('fio', '')
        address_a = request.POST.get('address_a', '')
        address_b = request.POST.get('address_b', '')
        gabarits = request.POST.get('gabarits', None)
        weigth = request.POST.get('weigth', None)

        if weigth is not None and weigth != '':
            response_type = requests.post('http://127.0.0.1:8000/customer/api/orders/', data={
                'fio': fio,
                'address_a': address_a,
                'address_b': address_b,
                'gabarits': gabarits,
                'weigth': float(weigth),
                'client': client,
                'status': None
            })
            redirect('my_orders')

    return render(request, template + '/add_order.html', context=context)