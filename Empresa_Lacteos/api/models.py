from django.db import models

# Create your models here.
class Vendedor(models.Model):
    nombre=models.CharField(max_length=100)
    cedula=models.CharField(max_length=15)
    
class Establecimiento(models.Model):
    nombre=models.CharField(max_length=100)
    tipo=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=30)
    
class Portafolio(models.Model):
    nombre=models.CharField(max_length=100)
    tipo=models.CharField(max_length=50)

class Producto(models.Model):
    nombre=models.CharField(max_length=100)
    detalle=models.TextField(null=True, blank=True)
    stock=models.CharField(max_length=10)

#En este modelo se relacionan el portafolio con los productos que pertenecen a este
class Rel_Producto_Portafolio(models.Model):
    portafolio=models.ForeignKey('Portafolio', on_delete=models.PROTECT,  related_name='portafolio_prod', null=True)
    producto=models.ForeignKey('Producto', on_delete=models.PROTECT,  related_name='prod_portafolio', null=True)

#En este modelo se relacionan el vendedor con los establecimientos que tiene a cargo
class Rel_Vendedor_Establecimiento(models.Model):
    Vendedor=models.ForeignKey('Vendedor', on_delete=models.PROTECT,  related_name='vendedor_est', null=True)
    Establecimiento=models.ForeignKey('Establecimiento', on_delete=models.PROTECT,  related_name='establecimiento_vend', null=True)
