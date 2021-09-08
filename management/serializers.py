from rest_framework.serializers import ModelSerializer, ImageField

from . import models


class SolicitudesReservaSerializer(ModelSerializer):
    class Meta:
        model = models.SolicitudesReserva
        fields = ["id", "name", "id_number", "description",
                  "number_of_persons", "reservation_date"]


class MenuSerializer(ModelSerializer):
    class Meta:
        model = models.Menu
        fields = ["id", "plate_name", "price",
                  "description", "available", "category","imagen"]
