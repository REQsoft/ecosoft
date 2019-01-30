from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Activity(models.Model):
    frequency_choices = (
        ('Diaria', 'Diaria'),
        ('Semanal', 'Semanal'),
        ('Mensual', 'Mensual'),
        ('Unica', 'Unica')
    )

    estados = (
        ('Pendiente', 'Pendiente'),
        ('Terminado', 'Terminado'),
        ('Expirado', 'Expirado'),
    )

    nombre = models.CharField(max_length=30, unique=True)
    responsable = models.ForeignKey(User, on_delete="PROTECTED")
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_terminacion = models.DateTimeField(blank=True, null=True)
    frecuencia = models.CharField(choices=frequency_choices, max_length=20)
    estado = models.CharField(choices=estados, max_length=20, default='Pendiente')

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'

    def __str__(self):
        return self.nombre + " ("+self.estado+")"
        

class Report(models.Model):
    actividad = models.ForeignKey(Activity, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_reporte = models.DateTimeField()
    
    class Meta:
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'

    def __str__(self):
        return str(self.actividad)


class Pending(models.Model):
    actividad = models.ForeignKey(Activity, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Actividad pendiente'
        verbose_name_plural = 'Actividades pendientes'

    def __str__(self):
        return self.activity.nombre

class Finish(models.Model):
    actividad = models.ForeignKey(Activity, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Actividad terminada'
        verbose_name_plural = 'Actividades terminadas'

    def __str__(self):
        return self.activity.nombre



