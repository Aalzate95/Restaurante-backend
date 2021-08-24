from django.shortcuts import render
from django.shortcuts import render
from . import models, serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.authentication import SessionAuthentication

# Create your views here.
class SolicitudesReservaViewSet(viewsets.ReadOnlyModelViewSet):
    #permission_classes = [IsAuthenticated]
    #authentication_classes=[SessionAuthentication]
    serializer_class = serializers.SolicitudesReservaSerializer

    def get_queryset(self):
        solicitudesReservas = models.SolicitudesReserva.objects.all()
        return solicitudesReservas