from django.urls import path

from  .views.api_views import ApiProductoList,ApiCatagoriaProductosList,ApiProductoDetail,GuardarPedido

urlpatterns = [
    path('api/obtener_productos', ApiProductoList.as_view()),
    path('api/obtener_categorias', ApiCatagoriaProductosList.as_view()),
    path('api/obtener_productos/<int:pk>/', ApiProductoDetail.as_view()),
    path('api/guardar_pedido', GuardarPedido.as_view()),

]