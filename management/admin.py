from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(SolicitudesReserva)
class SolicitudesReservaAdmin(admin.ModelAdmin):

    list_display = ('name', 'id_number', 'description', 'number_of_persons')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):

    list_display = ('plate_name', 'price', 'description',
                    'category', 'available')
