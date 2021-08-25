from django.db.models import Model, CASCADE, DO_NOTHING,SET_NULL
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
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class SolicitudesReserva(Model):
    name = CharField(max_length=255,blank=False)
    id_number = CharField(max_length=10,blank=False)
    description=CharField(max_length=1200,null=True,blank=True)
    number_of_persons = IntegerField(blank=True)
    reservation_date = DateTimeField(null=False, db_index=True)
    created_date = DateTimeField(auto_now_add=True, null=True, db_index=True)
    updated_date = DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-reservation_date"]
    
    def __str__(self):
        return f"{self.id_number,self.name,self.number_of_persons}"

class Mesa(Model):
    table_num = CharField(max_length=5,blank=False)
    num_chairs = CharField(max_length=10,blank=False)
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