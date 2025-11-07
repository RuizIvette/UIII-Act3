from django.db import models

# Create your models here.
class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    # ==========================================
# MODELO: Mascota (NUEVO)
# ==========================================
class Mascota(models.Model):
    mascota_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50) # Ej: Perro, Gato, Ave
    raza = models.CharField(max_length=50, blank=True, null=True) # Ej: Labrador, Siamés. Lo cambio a CharField.
    # Conexión con el modelo Cliente
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='mascotas')

    def __str__(self):
        # Puedes adaptar este string para que sea más informativo
        return f"{self.nombre} ({self.tipo}) - Dueño: {self.cliente.nombre} {self.cliente.apellido}"