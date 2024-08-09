from django.contrib import admin
from .models import Ubicacion, Habitat, Amenaza, Conservacion, Hostales, Especie

class HabitatInline(admin.TabularInline):
    model = Habitat
    extra = 1

class AmenazaInline(admin.TabularInline):
    model = Amenaza
    extra = 1

class ConservacionInline(admin.TabularInline):
    model = Conservacion
    extra = 1

@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'latitud', 'longitud')
    inlines = [HabitatInline, AmenazaInline, ConservacionInline]

@admin.register(Habitat)
class HabitatAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion')

@admin.register(Amenaza)
class AmenazaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion')

@admin.register(Conservacion)
class ConservacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion')

admin.site.register(Hostales)


admin.site.register(Especie)