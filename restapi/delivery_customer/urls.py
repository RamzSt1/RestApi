from django.urls import path, include
from rest_framework import routers

from delivery_customer.views import *

router = routers.DefaultRouter()
router.register(r'gabarits', GabaritsViewSet)
router.register(r'orders', OrdersViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('add_order', add_order, name='add_order'),
    path('orders', orders, name='orders'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('api/', include(router.urls)),
]