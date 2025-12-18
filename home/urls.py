from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("pago-diferido/", views.pago_diferido, name="pago_diferido"),
    path("pago-programado/", views.pago_programado, name="pago_programado"),
    path("debito/", views.debito, name="debito"),
    path("credito/", views.credito, name="credito"),
    path("suscripcion/", views.suscripcion, name="suscripcion"),
    path("puntaje/", views.puntaje, name="puntaje"),
]
