from django.contrib import admin
from .models import Producto, Pedido

admin.site.site_header = "Administración | Cafetería Karen"
admin.site.site_title = "Cafetería Karen"
admin.site.index_title = "Panel de administración"

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'categoria', 'disponible')
    list_filter = ('categoria', 'disponible')
    search_fields = ('nombre',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente_nombre', 'estado', 'total', 'fecha')
    list_filter = ('estado', 'fecha')
    search_fields = ('cliente_nombre',)
# Register your models here.
