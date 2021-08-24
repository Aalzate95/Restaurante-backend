from django.db.models import Model, CASCADE, DO_NOTHING,SET_NULL
from django.db.models import ForeignKey, OneToOneField, ManyToManyField
import uuid # Requerida para las instancias de libros únicos
from django.db.models import (
    CharField,
    IntegerField,
    FloatField,
    DateTimeField,
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
        return f"{self.id_number}"
