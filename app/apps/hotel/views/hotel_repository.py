
from ..models import Habitacion, FechaReserva, Reserva

def guardar_reserva(reserva_model):
    print("hola mundo")
    print(reserva_model)
    reserva = Reserva(
        estado_reserva=reserva_model["estado_reserva"],
        metodo_pago=reserva_model["metodo_pago"],
        cliente=reserva_model["cliente"],
        documento_identidad_cliente=reserva_model["documento_identidad_cliente"],
        monto_pagar=reserva_model["monto_pagar"]
    )
    reserva.save()
    return reserva


def guardar_fecha_reserva(reserva, fecha_reserva):
    for index, item in enumerate(fecha_reserva):
        habitacion = Habitacion.objects.get(pk=item["habitacion"])

        detalle = FechaReserva()
        detalle.reserva = reserva
        detalle.habitacion = habitacion
        detalle.fecha = item["fecha"]

        detalle.save()

    return FechaReserva.objects.filter(reserva=reserva)