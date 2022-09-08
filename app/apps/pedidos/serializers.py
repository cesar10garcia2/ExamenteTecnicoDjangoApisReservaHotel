from rest_framework import serializers
from .models import Producto, Categoria, Pedidos, DetallePedidos, Cliente



class CatagoriaProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id','nombre']

class ProductoSerializer(serializers.ModelSerializer):
    categoria = CatagoriaProductosSerializer()
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio','categoria']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id','nombre','celular','direccion']

class PedidosSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    class Meta:
        model = Pedidos
        fields = ['id','cliente']

class DetallePedidosSerializer(serializers.ModelSerializer):
    producto = Producto()
    pedido = Pedidos()
    class Meta:
        model = DetallePedidos
        fields = ['id','pedido', 'cantidad', 'precio_unitario','sub_total',"producto"]

class GuardarPedidosSerializer(serializers.ModelSerializer):
    producto = Producto()
    pedido = Pedidos()
    detalle = DetallePedidosSerializer(many=True)
    cliente = ClienteSerializer()
    class Meta:
        model = DetallePedidos
        fields = ['id', 'cantidad', 'precio_unitario','sub_total','cliente','pedido', 'detalle']
