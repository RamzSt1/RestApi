from rest_framework import serializers

from delivery_customer.models import *


class SerializerGabarits(serializers.ModelSerializer):
    class Meta:
        model = Gabarits
        fields = ('id', 'name',)

class SerializerOrders(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('date', 'fio', 'address_a', 'address_b', 'gabarits', 'weigth', 'status', 'client')