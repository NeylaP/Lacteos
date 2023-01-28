from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.db.models import Q

from .models import Establecimiento, Portafolio, Producto, Rel_Producto_Portafolio, Rel_Vendedor_Establecimiento, Vendedor
import json

# Create your views here.



class VendedorView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        vendedores=list(Vendedor.objects.values())
        if len(vendedores)>0:
            data={'mensaje':'Success', 'vendedores':vendedores}
        else:
            data={'mensaje': 'No se encontraron Vendedores'}
        return JsonResponse(data)
    
    def post(self, request):
        jd=json.loads(request.body)
        try:
            Vendedor.objects.get(cedula=jd["cedula"])
        except (KeyError, Vendedor.DoesNotExist):
            Vendedor.objects.create(nombre=jd['nombre'],cedula=jd['cedula'])
            data={'mensaje':'Datos Enviados'}
            return JsonResponse(data)
        else:
            data={'mensaje':'La cedula ingresada ya se encuentra en nuestra base de datos'}
            return JsonResponse(data)

class EstablecimientoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        establecimientos=list(Establecimiento.objects.values())
        if len(establecimientos)>0:
            data={'mensaje':'Success', 'establecimientos':establecimientos}
        else:
            data={'mensaje': 'No se encontraron establecimientos'}
        return JsonResponse(data)
    
    def post(self, request):
        jd=json.loads(request.body)
        Establecimiento.objects.create(nombre=jd['nombre'],ciudad=jd['ciudad'],tipo=jd['tipo'])
        data={'mensaje':'Datos Enviados'}
        return JsonResponse(data)

class ProductoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        productos=list(Producto.objects.values())
        if len(productos)>0:
            data={'mensaje':'Success', 'productos':productos}
        else:
            data={'mensaje': 'No se encontraron productos'}
        return JsonResponse(data)
    
    def post(self, request):
        jd=json.loads(request.body)
        Producto.objects.create(nombre=jd['nombre'],detalle=jd['detalle'],stock=jd['stock'])
        data={'mensaje':'Datos Enviados'}
        return JsonResponse(data)

class PortafolioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        portafolios=list(Portafolio.objects.values())
        if len(portafolios)>0:
            data={'mensaje':'Success', 'portafolios':portafolios}
        else:
            data={'mensaje': 'No se encontraron portafolios'}
        return JsonResponse(data)
    
    def post(self, request):
        jd=json.loads(request.body)
        Portafolio.objects.create(nombre=jd['nombre'],tipo=jd['tipo'])
        data={'mensaje':'Datos Enviados'}
        return JsonResponse(data)

# Aqui se vizualizan las acciones de las relaciones entre portafolios y productos
class RelProdPortView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        relaciones=list(Rel_Producto_Portafolio.objects.values())
        if len(relaciones)>0:
            data={'mensaje':'Success', 'relaciones':relaciones}
        else:
            data={'mensaje': 'No se encontraron relaciones'}
        return JsonResponse(data)
    
    def post(self, request):
        jd=json.loads(request.body)
        try:
            Rel_Producto_Portafolio.objects.get(Q(portafolio=jd["portafolio"]), Q(producto=jd["producto"]))
        except (KeyError, Rel_Producto_Portafolio.DoesNotExist):
            portafolio=Portafolio.objects.get(id=jd['portafolio'])
            producto=Producto.objects.get(id=jd['producto'])
            Rel_Producto_Portafolio.objects.create(portafolio=portafolio,producto=producto)
            data={'mensaje':'Datos enviados'}
            return JsonResponse(data)
        else:
            data={'mensaje':'Esta relacion ya se encuentra en nuestra base de datos'}
            return JsonResponse(data)

# Aqui se vizualizan las acciones de las relaciones entre vendedor y establecimiento
class RelVendEstabView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        relaciones=list(Rel_Vendedor_Establecimiento.objects.values())
        if len(relaciones)>0:
            data={'mensaje':'Success', 'relaciones':relaciones}
        else:
            data={'mensaje': 'No se encontraron relaciones'}
        return JsonResponse(data)
    
    def post(self, request):
        jd=json.loads(request.body)
        try:
            Rel_Vendedor_Establecimiento.objects.get(Q(Vendedor=jd["vendedor"]), Q(Establecimiento=jd["establecimiento"]))
        except (KeyError, Rel_Vendedor_Establecimiento.DoesNotExist):
            vendedor=Vendedor.objects.get(id=jd['vendedor'])
            establecimiento=Establecimiento.objects.get(id=jd['establecimiento'])
            Rel_Vendedor_Establecimiento.objects.create(Vendedor=vendedor,Establecimiento=establecimiento)
            data={'mensaje':'Datos Enviados'}
            return JsonResponse(data)
        else:
            data={'mensaje':'Esta relacion ya se encuentra en nuestra base de datos'}
            return JsonResponse(data)