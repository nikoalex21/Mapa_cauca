from django.db import models

class Habitat(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    ubicacion = models.ForeignKey('Ubicacion', on_delete=models.CASCADE, related_name='habitats')

    def __str__(self):
        return self.nombre

class Amenaza(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    ubicacion = models.ForeignKey('Ubicacion', on_delete=models.CASCADE, related_name='amenazas')

    def __str__(self):
        return self.nombre

class Conservacion(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    ubicacion = models.ForeignKey('Ubicacion', on_delete=models.CASCADE, related_name='conservaciones')

    def __str__(self):
        return self.nombre

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    imagen = models.ImageField(upload_to='imagen', null=True, blank=True)


    def __str__(self):
        return self.nombre

class Hostales(models.Model):
    nombreHostal = models.CharField(max_length=200)
    descripcionHostal = models.TextField()
    latitudHostal = models.DecimalField(max_digits=9, decimal_places=6)
    longitudHostal = models.DecimalField(max_digits=9, decimal_places=6)
    imagenHostal = models.ImageField(upload_to='hostales', null=True, blank=True)
    precioHostal = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
    
    
class Especie(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    latitud = models.FloatField()
    longitud = models.FloatField()
    
    def __str__(self):
        return self.nombre

