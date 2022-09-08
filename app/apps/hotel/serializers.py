from rest_framework import serializers
from .models import Habitacion, FechaReserva, Reserva
import datetime

class FechasActivasReservaSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        fecha_min = datetime.date.today()
        print(fecha_min)
        data = data.filter(fecha__gte = fecha_min)
        return super(FechasActivasReservaSerializer, self).to_representation(data)

class FechaReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FechaReserva
        list_serializer_class = FechasActivasReservaSerializer
        fields = ['id', 'fecha', 'habitacion', 'reserva']
        read_only_fields = ('fecha',)

class HabitacionSerializer(serializers.ModelSerializer):
    fecha_reservas = FechaReservaSerializer(many=True)


    class Meta:
        model = Habitacion
        fields = ['id', 'nombre', 'fecha_reservas']

class ReservaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reserva
        fields = ['id', 'estado_reserva', 'metodo_pago', 'cliente',
                  'documento_identidad_cliente', 'monto_pagar']


class FechaReservaGuardarSerializer(serializers.ModelSerializer):
    class Meta:
        model = FechaReserva
        fields = ['id', 'fecha', 'habitacion']

class GuardarReservaSerializer(serializers.ModelSerializer):
    reserva = ReservaSerializer()
    fechas = FechaReservaGuardarSerializer(many=True)
    habitacion = Habitacion()
    class Meta:
        model = FechaReserva
        fields = ['id', 'reserva', 'fechas']