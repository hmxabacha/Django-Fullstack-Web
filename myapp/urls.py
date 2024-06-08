from . import views
from django.urls import path

urlpatterns = [
    path("",views.booking,name='booking'),
    path("reservations/",views.reservations,name='reservations'),
]
