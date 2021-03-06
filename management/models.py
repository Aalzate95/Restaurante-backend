from django.db.models import Model, CASCADE, DO_NOTHING, SET_NULL
from django.db.models import ForeignKey, OneToOneField, ManyToManyField
from django.db.models import (
    CharField,
    IntegerField,
    FloatField,
    DateTimeField,
    TimeField,
    BooleanField,
    FileField,
    UUIDField,
    DateField
)
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse


class SolicitudesReserva(Model):
    name = CharField(max_length=255, blank=False)
    id_number = CharField(max_length=10, blank=False)
    description = CharField(max_length=1200, null=True, blank=True)
    number_of_persons = IntegerField(blank=True)
    reservation_date = DateTimeField(null=False, db_index=True)
    status_choices = (("Asistió", "Asistió"),("Faltó","Faltó"),("Cancelado","Cancelado"),("Pendiente","Pendiente"))
    status = CharField(max_length=50,choices=status_choices,default="Pendiente")
    created_date = DateTimeField(auto_now_add=True, null=True, db_index=True)
    updated_date = DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-reservation_date"]

    def __str__(self):
        return f"{self.id_number,self.name,self.number_of_persons}"

class Mesa(Model):
    table_num = CharField(max_length=5,blank=False)
    num_chairs = IntegerField(blank=False)
    description=CharField(max_length=1200,null=True,blank=True)
    location=CharField(max_length=1200,null=True,blank=True)

    def __str__(self):
        return f"{self.table_num,self.num_chairs,self.description,self.location}"

class Horario(Model):
    id_number = CharField(max_length=10,blank=False)
    start_time = TimeField(null=False)
    end_time = TimeField(null=False)

    def __str__(self):
        return f"{self.id_number,self.start_time,self.end_time}"

class Disponibilidad(Model):
    id_number = CharField(max_length=10,blank=False)
    table_id = CharField(max_length=5,blank=False)
    schedule_id = CharField(max_length=10,blank=False)
    status=CharField(max_length=1200,null=True,blank=True)

    def __str__(self):
        return f"{self.id_number,self.table_id,self.schedule_id,self.status}"

class Menu(Model):
    plate_name = CharField(max_length=255, blank=False)
    price = FloatField(blank=False)
    description = CharField(max_length=1200, null=True, blank=True)
    available = BooleanField(blank=False)
    imagen = CharField(max_length=500,blank=False,default="")
    category_choices = (("Desayuno", "Desayuno"), ("Plato Fuerte",
                        "Plato Fuerte"), ("Postre", "Postre"), ("Bebidas", "Bebidas"))
    category = CharField(max_length=75, blank=False,choices=category_choices, default="Plato Fuerte")
    created_date = DateTimeField(auto_now_add=True, null=True, db_index=True)
    updated_date = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.plate_name,self.price,self.description, self.category, self.available}"
