from django.http import Http404
from rest_framework import generics
from ..models import Habitacion, FechaReserva
from .hotel_repository import guardar_reserva, guardar_fecha_reserva
from ..serializers import HabitacionSerializer, GuardarReservaSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class ApiHabitacionList(generics.ListAPIView):
    serializer_class = HabitacionSerializer

    def get_queryset(self):
        """
        Obtener una lista de productos con filtrado por categoria o nombre
        """
        nombre = self.request.GET.get('nombre')
        if nombre == None:
            nombre = ''
        object_list = Habitacion.objects.filter(
            nombre__icontains=nombre).order_by('nombre')
        return object_list

class GuardarReserva(APIView):
    def post(self, request, format=None):
        serializer = GuardarReservaSerializer(data=request.data)
        if serializer.is_valid():
            for index, item in enumerate(serializer.data["fechas"]):
                habitacion = Habitacion.objects.get(pk=item["habitacion"])
                if FechaReserva.objects.filter(fecha=item["fecha"]).filter(
                        habitacion=habitacion).exists():
                    return Response("La habitacion esta ocupada en esas fechas.")

            reserva = guardar_reserva(serializer.data["reserva"])
            guardar_fecha_reserva(reserva, serializer.data["fechas"])


            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)