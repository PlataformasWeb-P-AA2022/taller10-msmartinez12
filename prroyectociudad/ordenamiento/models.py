from django.db import models

# Create your models here.

class Parroquia(models.Model):
    opciones_tipo_parroquia = (
        ('urbana', 'Parroquia Urbana'),
        ('rural', 'Parroquia Rural'),
        )

    nombre = models.CharField(max_length=50)
    tipo_parroquia = models.CharField(max_length=30, \
            choices=opciones_tipo_parroquia) 
    
    def __str__(self):
        return "%s | %s" % (self.nombre, 
                self.tipo_parroquia,
        )

class Barrio(models.Model):
    opciones_numero_parques = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    )
    nombre = models.CharField(max_length=50)
    numero_viviendas = models.IntegerField("número de viviendas")
    numero_parques = models.IntegerField("número de parques", \
        choices=opciones_numero_parques)
    numero_edificios = models.IntegerField("número de edificios")
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE,
            related_name="nombres_barrios")
    
    def __str__(self):
        return "Nombre: %s - Num viviendas: %d - Num parques %d - Num edificios: %d - Parroquia: %s" % (self.nombre, 
                self.numero_viviendas,
                self.numero_parques,
                self.numero_edificios,
                self.parroquia
        )

