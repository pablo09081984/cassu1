from django import forms

WALLETS = [
    ("mercadopago", "Mercado Pago"),
    ("uala", "Ualá"),
    ("brubank", "Brubank"),
    ("prex", "Prex"),
    ("naranja_x", "Naranja X"),
]

class PagoForm(forms.Form):
    email = forms.EmailField(label="Email")
    wallet = forms.ChoiceField(choices=WALLETS, label="Billetera")
    monto = forms.DecimalField(label="Monto", min_value=1, decimal_places=2, max_digits=12)
    referencia = forms.CharField(label="Referencia", required=False, max_length=50)

class PagoProgramadoForm(PagoForm):
    fecha = forms.DateField(label="Fecha de pago", widget=forms.DateInput(attrs={"type": "date"}))

class SuscripcionForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=80)
    email = forms.EmailField(label="Email")
    telefono = forms.CharField(label="Teléfono", required=False, max_length=30)
