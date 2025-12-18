from django.db import models

class Suscripcion(models.Model):
    email = models.EmailField()
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
