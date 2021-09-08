from django.conf.urls import url
from . import views
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'solicitudesReserva',views.SolicitudesReservaViewSet, basename='SolicitudesReserva')
router.register(r'menu', views.MenuViewSet, basename='Menu')

urlpatterns = [
    path('', include(router.urls)),

]
