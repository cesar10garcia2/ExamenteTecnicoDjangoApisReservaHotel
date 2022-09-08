from django.contrib import admin
from .models import Categoria, Producto, Cliente, Pedidos, DetallePedidos

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)

admin.site.register(Cliente)
admin.site.register(Pedidos)
admin.site.register(DetallePedidos)
