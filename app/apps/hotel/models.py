from django.db import models

ESTADO = (
    ('0', 'Eliminado'),
    ('1', 'Activo'),
)
class Habitacion(models.Model):
    nombre = models.CharField(max_length=100,unique=True, verbose_name="Habitacion")
    estado = models.CharField(
        max_length=1, choices=ESTADO, default=1, editable=False)

    def __str__(self):
        return self.nombre

ESTADO_RESERVA = (
    ('PE', 'Pendiente'),
    ('PA', 'Pagado'),
    ('EL', 'Eliminado'),
)

METODO_PAGO = (
    ('EFECTIVO', 'EFECTIVO'),
    ('YAPE', 'YAPE'),
    ('TRANSFERENCIA', 'TRANSFERENCIA'),
)


class Reserva(models.Model):
    estado_reserva = models.CharField('Estado',
        max_length=2, choices=ESTADO_RESERVA, default='PE', editable=True)
    metodo_pago = models.CharField('Metodo de pago',
        max_length=15, choices=METODO_PAGO, default='PE', editable=True)
    cliente = models.CharField(
        'Cliente',
        max_length=100, blank=False, null=False)
    documento_identidad_cliente = models.CharField(
        'Documento Identidad',
        max_length=15, blank=False, null=False)
    monto_pagar = models.DecimalField(
        'Monto Pagar',
        max_digits=19, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return self.nombre


class FechaReserva(models.Model):
    fecha = models.DateField()
    habitacion = models.ForeignKey(
        Habitacion, on_delete=models.PROTECT,
        related_name = 'fecha_reservas',
        verbose_name="Habitacion"
    )
    reserva = models.ForeignKey(
        Reserva, on_delete=models.PROTECT,
        verbose_name="Reserva"
    )