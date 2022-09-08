from django.urls import path

from .views.api_views import ApiHabitacionList, GuardarReserva, ApiReservaDetail

urlpatterns = [
    path('api/obtener_habitaciones', ApiHabitacionList.as_view()),
    path('api/obtener_reserva/<int:pk>/', ApiReservaDetail.as_view()),
    path('api/guardar_reserva', GuardarReserva.as_view()),
]