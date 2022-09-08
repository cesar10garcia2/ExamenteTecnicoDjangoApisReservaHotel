# ExamenteTecnicoDjangoApisReservaHotel
Apis para reservar habitaciones de un hotel.

#APIS
# API GET PARA OBTENER LAS HABITACIONES Y SUS DIAS RESERVADOS
/hotel/api/obtener_habitaciones

# ESTRUCTURA SALIDA OBTENER LAS HABITACIONES

    [
        {
            "id": 1,
            "nombre": "HABITACION 01",
            "fecha_reservas": [
                {
                    "id": 1,
                    "fecha": "2022-09-26",
                    "habitacion": 1,
                    "reserva": 11
                },
                {
                    "id": 2,
                    "fecha": "2022-09-27",
                    "habitacion": 1,
                    "reserva": 11
                }
            ]
        },
        {
            "id": 2,
            "nombre": "HABITACION 02",
            "fecha_reservas": []
        },
        {
            "id": 3,
            "nombre": "HABITACION 03",
            "fecha_reservas": []
        },
        {
            "id": 4,
            "nombre": "HABITACION 04",
            "fecha_reservas": []
        }
    ]

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

# API GET DETALLE RESERVA
/hotel/api/obtener_reserva/11/
# SALIDA DETALLE RESERVA
    {
        "id": 11,
        "estado_reserva": "PE",
        "metodo_pago": "EFECTIVO",
        "cliente": "CESAR ROBERTO GARCIA",
        "documento_identidad_cliente": "76435132",
        "monto_pagar": "150.00",
        "reservas": [
            {
                "id": 1,
                "fecha": "2022-09-26",
                "habitacion": 1,
                "reserva": 11
            },
            {
                "id": 2,
                "fecha": "2022-09-27",
                "habitacion": 1,
                "reserva": 11
            }
        ]
    }

# VALIDACIONES CONSIDERADAS
- No se puede volver a reservar una habitacion con una fecha reservada.
- En el listado de habitaciones muestra las fechas reservadas del día actual para adelante.