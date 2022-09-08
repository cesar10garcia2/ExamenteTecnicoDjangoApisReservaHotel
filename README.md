# ExamenteTecnicoDjangoApisReservaHotel
Apis para reservar habitaciones de un hotel.

#APIS
# API GET PARA OBTENER LAS HABITACIONES Y SUS DIAS RESERVADOS
/hotel/api/obtener_habitaciones

# API POS PARA REGISTRAR LA RESERVA
/hotel/api/guardar_reserva
# ESTRUCTURA PARA ENVIAR A LA API


    {
        "fechas":[ 
            {
                "fecha" : "2022-09-26",
                "habitacion": 1
            },
            {
                "fecha" : "2022-09-27",
                "habitacion": 1
            }
        ],
        "reserva": {
            "estado_reserva" : "PE",
            "metodo_pago" : "EFECTIVO",
            "cliente":"CESAR ROBERTO GARCIA",
            "documento_identidad_cliente" : "76435132",
            "monto_pagar" : 150
        }
    }

# VALIDACIONES CONSIDERADAS
- No se puede volver a reservar una habitacion con una fecha reservada.
- En el listado de habitaciones muestra las fechas reservadas del día actual para adelante.