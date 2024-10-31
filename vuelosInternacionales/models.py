from django.db import models

# Create your models here.

class Aerolinea(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    
class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    
class Vuelo(models.Model):
    aerolinea = models.ForeignKey(Aerolinea, on_delete=models.CASCADE)
    origen = models.ForeignKey(Pais, related_name='pais_origen', on_delete=models.CASCADE)
    destino = models.ForeignKey(Pais, related_name='pais_destino', on_delete=models.CASCADE)
    hora_salida = models.DateTimeField()
    hora_llegada = models.DateTimeField()
    asientos_disponibles = models.IntegerField()
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    fono = models.CharField(max_length=15) 

class Ticket(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)
    numero_asiento = models.CharField(max_length=5)
    fecha_reserva = models.DateTimeField(auto_now_add=True)       
           