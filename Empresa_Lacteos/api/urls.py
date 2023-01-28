from django.urls import path

from .views import EstablecimientoView, PortafolioView, ProductoView, RelProdPortView, RelVendEstabView, VendedorView

urlpatterns = [
    path('vendedor/', VendedorView.as_view(), name='vendedores_list'),
    path('establecimiento/', EstablecimientoView.as_view(), name='establecimiento_list'),
    path('portafolio/', PortafolioView.as_view(), name='portafolio_list'),
    path('producto/', ProductoView.as_view(), name='producto_list'),
    path('rel_producto_portafolio/', RelProdPortView.as_view(), name='rel_pro_list'),
    path('rel_vendedor_establecimiento/', RelVendEstabView.as_view(), name='rel_vend_list'),
]
