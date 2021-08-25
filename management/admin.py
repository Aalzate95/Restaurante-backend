from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(SolicitudesReserva)
class SolicitudesReservaAdmin(admin.ModelAdmin):
   
    list_display = ('name', 'id_number', 'description','number_of_persons')

@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
   
    list_display = ('table_num','num_chairs','description','location')

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
   
    list_display = ('id_number','start_time','end_time')

@admin.register(Disponibilidad)
class DisponibilidadAdmin(admin.ModelAdmin):
   
    list_display = ('id_number','table_id','schedule_id','status')