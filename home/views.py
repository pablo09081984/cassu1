from django.shortcuts import render, redirect
from .forms import PagoForm, PagoProgramadoForm, SuscripcionForm

WALLET_URLS = {
    "mercadopago": "https://www.mercadopago.com.ar/",
    "uala": "https://www.uala.com.ar/",
    "brubank": "https://www.brubank.com/",
    "prex": "https://www.prexcard.com.ar/",
    "naranja_x": "https://www.naranjax.com/",
}

def index(request):
    return render(request, "home/index.html")

def pago_diferido(request):
    if request.method == "POST":
        form = PagoForm(request.POST)
        if form.is_valid():
            wallet = form.cleaned_data["wallet"]
            return redirect(WALLET_URLS.get(wallet, "/"))
    else:
        form = PagoForm()
    return render(request, "home/pago_diferido.html", {"form": form})

def pago_programado(request):
    if request.method == "POST":
        form = PagoProgramadoForm(request.POST)
        if form.is_valid():
            wallet = form.cleaned_data["wallet"]
            return redirect(WALLET_URLS.get(wallet, "/"))
    else:
        form = PagoProgramadoForm()
    return render(request, "home/pago_programado.html", {"form": form})

def debito(request):
    return render(request, "home/debito.html")

def credito(request):
    return render(request, "home/credito.html")

def suscripcion(request):
    if request.method == "POST":
        form = SuscripcionForm(request.POST)
        if form.is_valid():
            # por ahora no guardamos en DB, solo confirmación
            return render(request, "home/suscripcion.html", {"form": SuscripcionForm(), "ok": True})
    else:
        form = SuscripcionForm()
    return render(request, "home/suscripcion.html", {"form": form})

def puntaje(request):
    return render(request, "home/puntaje.html")
