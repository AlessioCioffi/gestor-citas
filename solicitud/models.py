from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Solicitud(models.Model):
    
    TYPE_CHOICES = (
        ('Multa', 'Multa'),
        ('Retiro', 'Retiro'),
        ('Entrega', 'Entrega'),
        ('Carnet', 'Carnet'),
        ('Renovar', 'Renovar')
    )

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True)
    name = models.CharField(verbose_name='Nombre',max_length=200)
    surname = models.CharField(verbose_name='Apellido', max_length=200)
    n_document = models.CharField(verbose_name='DNI o NIE', max_length=50)
    order = models.SmallIntegerField(verbose_name='Orden',default=0)
    description = models.CharField(verbose_name='Tramite', max_length=200, choices=TYPE_CHOICES)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creación')
    update = models.DateTimeField(auto_now=True, verbose_name='Edición')

    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'
        ordering = ['order']

    def __str__(self):
        return self.type
