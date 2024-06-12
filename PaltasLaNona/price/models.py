from django.db import models

# Create your models here.
class tipo_producto(models.Model):
    nombre = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.nombre

class producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)
    tipo_producto_id = models.ForeignKey(tipo_producto, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class tipo_entrega(models.Model):
    nombre = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.nombre
    
class tipo_cotizacion(models.Model):
    descripcion = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)
    peso_minimo = models.IntegerField()
    peso_maximo = models.IntegerField()
    
    def __str__(self):
        return self.descripcion
    
class unidad_medida(models.Model):
    nombre = models.CharField(max_length=50)
    abreviacion = models.CharField(max_length=10)
    multiplo = models.IntegerField()
    
    def __str__(self):
        return self.nombre

class solicitud_cotizacion(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=False)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad = models.BigIntegerField()
    unidad_medida = models.ForeignKey(unidad_medida, on_delete=models.CASCADE)
    contacto = models.TextField(blank=True)
    direccion_entrega = models.TextField(blank=True)
    tipo_cotizacion_id = models.ForeignKey(tipo_cotizacion, on_delete=models.CASCADE)
    tipo_entrega_id = models.ForeignKey(tipo_entrega, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.contacto
    
class cotizacion(models.Model):
    solicitud_id = models.ForeignKey(solicitud_cotizacion, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    venta = models.BooleanField(default=False)
    usuario_id = models.TextField(max_length=100)
    unidad_medida = models.ForeignKey(unidad_medida, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.solicitud_id