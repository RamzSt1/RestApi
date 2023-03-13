from django.contrib import admin
from delivery_customer.models import *
# Register your models here.

@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = list_display
    search_fields = list_display
    
@admin.register(Gabarits)
class AdminGabarits(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = list_display
    search_fields = list_display
    
@admin.register(Status)
class AdminStatus(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = list_display
    search_fields = list_display

@admin.register(Orders)
class AdminOrders(admin.ModelAdmin):
    list_display = ['customer', 'client', 'date', 'fio', 'address_a', 'address_b', 'gabarits', 'weigth', 'status', 'car']
    list_display_links = list_display
    search_fields = list_display
