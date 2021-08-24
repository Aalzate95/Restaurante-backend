from django.contrib import admin
from .models import SolicitudesReserva
# Register your models here.

@admin.register(SolicitudesReserva)
class SolicitudesReservaAdmin(admin.ModelAdmin):
   
    list_display = ('name', 'id_number', 'description','number_of_persons')