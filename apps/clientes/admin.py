from django.contrib import admin

# Register your models here.
from .models import Cliente, Categoria, Producto


admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Producto)
