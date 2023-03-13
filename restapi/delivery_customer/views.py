import datetime

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from delivery_customer.apps import template
from delivery_customer.forms import RegisterForms
from delivery_customer.models import Gabarits, Orders, Car, Status
from delivery_customer.serializers import SerializerGabarits, SerializerOrders


@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login')
def orders(request):
    context = {}
    orders = Orders.objects.all()
    print(orders)
    context.update({'orders': orders})
    return render(request, template + '/orders.html', context=context)

@login_required(login_url='/login')
def index(request):
    context = {}
    return render(request, template + '/index.html', context=context)

@login_required(login_url='/login')
def add_order(request):
    context = {}
    gabarits = Gabarits.objects.all()
    car = Car.objects.all()
    status = Status.objects.all()

    context.update({'gabarits': gabarits})
    context.update({'car': car})
    context.update({'status': status})

    edit_id = request.GET.get('edit_id')
    if edit_id is not None:
        order = Orders.objects.get(id=int(edit_id))
        context.update({'order_data': [order.fio, order.address_a, order.address_b, str(order.gabarits), str(order.weigth),
                                       str(order.car), str(order.status)]})

    if request.POST:
        fio = request.POST.get('fio', '')
        address_a = request.POST.get('address_a', '')
        address_b = request.POST.get('address_b', '')
        gabarits = Gabarits.objects.get(id=int(request.POST.get('gabarits')))
        weigth = float(request.POST.get('weigth', 0.0))
        car = Car.objects.get(id=int(request.POST.get('car')))
        status = Status.objects.get(id=int(request.POST.get('status')))

        new_order = Orders(customer=request.user, date=datetime.datetime.now(), fio=fio, address_a=address_a,
                           address_b=address_b, gabarits=gabarits, weigth=weigth, car=car, status=status)

        if edit_id is not None:
            new_order = Orders.objects.get(id=int(edit_id))
            new_order.fio = fio
            new_order.address_a = address_a
            new_order.address_b = address_b
            new_order.gabarits = gabarits
            new_order.weigth = weigth
            new_order.car = car
            new_order.status = status

        new_order.save()
        return redirect('orders')

    return render(request, template + '/add_order.html', context=context)

class LoginUser(LoginView):
    form_class = RegisterForms.LoginUserForm
    template_name = template + '/login.html'

    def get_success_url(self):
        return reverse_lazy('index')

class GabaritsViewSet(mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Gabarits.objects.all().order_by('id')
    serializer_class = SerializerGabarits

class OrdersViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    GenericViewSet):
    queryset = Orders.objects.all().order_by('id')
    serializer_class = SerializerOrders
