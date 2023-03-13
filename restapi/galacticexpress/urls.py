from django.urls import path

from galacticexpress.views import *

urlpatterns = [
    path('', index, name='index'),
    path('my_orders', orders, name='my_orders'),
    path('new_order', new_order, name='new_order'),

]