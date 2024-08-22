# admin.py

from django.contrib import admin
from .models import ContractData

@admin.register(ContractData)
class ContractDataAdmin(admin.ModelAdmin):
    list_display = ('ciudad', 'locador_nombre')  # Muestra estos campos en la lista del admin
    search_fields = ('ciudad', 'locador_nombre')  # Permite búsqueda por estos campos
