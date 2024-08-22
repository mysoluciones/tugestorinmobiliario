from django.urls import path
from .views import home, generate_contract, generate_gastos_contract, generate_reserva_compra_contract

urlpatterns = [
    path('', home, name='home'),
    path('generate-contract/', generate_contract, name='generate_contract'),
    path('generate-gastos/', generate_gastos_contract, name='generate_gastos_contract'),
    path('generate-reserva-compra/', generate_reserva_compra_contract, name='generate_reserva_compra_contract'),
]
