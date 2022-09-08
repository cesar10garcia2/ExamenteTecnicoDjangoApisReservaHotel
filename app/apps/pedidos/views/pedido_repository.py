
from ..models import Pedidos, Cliente, DetallePedidos, Producto

def guardar_cliente(cliente):
    cliente = Cliente(
        nombre=cliente["nombre"],
        celular=cliente["celular"],
        direccion=cliente["direccion"]
    )
    cliente.save()
    return cliente

def guardar_pedido(cliente):
    pedido = Pedidos(
        cliente=cliente
    )
    pedido.save()
    return pedido

def guardar_detalle_pedido(pedido, detalle):

    total_bruto = 0

    for index, item in enumerate(detalle):
        producto_temp = Producto.objects.get(pk=item["producto"])

        detalle = DetallePedidos()
        detalle.pedido = pedido
        detalle.producto = producto_temp
        detalle.precio = float(producto_temp.precio)
        detalle.cantidad = float(item["cantidad"])
        detalle.sub_total = float(producto_temp.precio) * float(item["cantidad"])

        detalle.save()
        total_bruto = detalle.sub_total + total_bruto



    pedido.total_bruto = total_bruto
    pedido.save()

    return DetallePedidos.objects.filter(pedido=pedido)