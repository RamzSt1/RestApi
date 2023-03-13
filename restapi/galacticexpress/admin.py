from django.contrib import admin
from galacticexpress.models import *

@admin.register(News)
class AdminCar(admin.ModelAdmin):
    list_display = ['title', 'text']
    list_display_links = list_display
    search_fields = list_display