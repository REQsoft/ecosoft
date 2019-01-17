from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Activity(models.Model):
    frequency_choices = (
        ('daily', 'Diaria'),
        ('weekly', 'Semanal'),
        ('monthly', 'Mensual'),
        ('unique', 'Unica')
    )

    states = (
        ('1', 'Pendiente'),
        ('2', 'En proceso'),
        ('3', 'Terminado'),
    )

    name = models.CharField(max_length=30, unique=True)
    responsible = models.ForeignKey(User, on_delete="PROTECTED")
    description = models.TextField()
    frequency = models.CharField(choices=frequency_choices, max_length=20)
    date = models.DateTimeField()
    state = models.CharField(choices=states, max_length=20, default='1')

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    def __str__(self):
        if self.state == '1':
            state = self.states[0][1]
        elif self.state == '2':
            state = self.states[1][1]
        else:
            state = self.states[2][1]
        return self.name + " ("+state+")"


class Report(models.Model):
    activity = models.OneToOneField(Activity, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField()
    
    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'

    def __str__(self):
        return str(self.activity)

