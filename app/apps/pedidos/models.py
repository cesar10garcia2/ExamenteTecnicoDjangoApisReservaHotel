from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100,unique=True, verbose_name="Categoria")

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT,
        verbose_name="Categoria", null=True
    )
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Producto")
    precio = models.DecimalField(
        'Precio',
        max_digits=13, decimal_places=2, default=0, blank=False, null=False)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Categoria")
    celular = models.CharField(max_length=12, verbose_name="Celular")
    direccion = models.CharField(max_length=100, verbose_name="Direccion")

    def __str__(self):
        return self.nombre

class Pedidos(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.PROTECT,
        verbose_name="Cliente", null=True
    )
    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    total_bruto = models.DecimalField(
        'Total Bruto',
        max_digits=13, decimal_places=2, default=0, blank=False, null=False)


class DetallePedidos(models.Model):
    producto = models.ForeignKey(
        Producto, on_delete=models.PROTECT,
        verbose_name="Producto", null=True
    )
    pedido = models.ForeignKey(
        Pedidos, on_delete=models.PROTECT,
        verbose_name="Pedido", null=True
    )
    cantidad = models.DecimalField(
        'Cantidad',
        max_digits=13, decimal_places=2, default=0, blank=False, null=False)

    precio_unitario = models.DecimalField(
        'Precio Unitario',
        max_digits=13, decimal_places=2, default=0, blank=False, null=False)

    sub_total = models.DecimalField(
        'SubTotal',
        max_digits=13, decimal_places=2, default=0, blank=False, null=False)


# 1- Listar Categorías
# 2- Detalle la categoría y sus respectivos productos ordenado por: mas vendidos, por precio o por nombre
# 3- Agregar al carrito de compras y mostrar sus items
# 4- Pedido donde recibe los datos del cliente y su carrito de compras respectivo
