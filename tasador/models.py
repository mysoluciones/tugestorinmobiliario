from django.db import models

class ContractData(models.Model):
    ciudad = models.CharField(max_length=100)
    fecha = models.DateField()
    locador_nombre = models.CharField(max_length=100)
    locador_dni = models.CharField(max_length=20)
    telefono_locador = models.CharField(max_length=15)
    mail_locador = models.EmailField()
    nacionalidad_locador = models.CharField(max_length=50)
    locador_direccion = models.CharField(max_length=255)
    ciudaddondevive_locador = models.CharField(max_length=100)
    provincia_locador = models.CharField(max_length=100)
    locatario_nombre = models.CharField(max_length=100)
    locatario_dni = models.CharField(max_length=20)
    mail_locatario = models.EmailField()
    telefono_locatario = models.CharField(max_length=15)
    superficie_inmueble = models.CharField(max_length=100)
    direccion_inmueble = models.CharField(max_length=255)
    colorcasa = models.CharField(max_length=50)
    tipo_pintura = models.CharField(max_length=50)
    marca_pintura = models.CharField(max_length=50)
    caracteristicas = models.TextField()
    alquiler_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    aumento = models.DecimalField(max_digits=5, decimal_places=2)
    meses = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    garantias = models.TextField()

    def __str__(self):
        return f"Contrato {self.ciudad} - {self.locador_nombre}"
    
from django.db import models

class GastosData(models.Model):
    direccion = models.CharField(max_length=255)
    parte = models.CharField(max_length=100)
    tipo_operacion = models.CharField(max_length=100)
    pago_contado = models.DecimalField(max_digits=10, decimal_places=2)
    financiacion = models.DecimalField(max_digits=10, decimal_places=2)
    honorarios = models.DecimalField(max_digits=10, decimal_places=2)
    condiciones = models.TextField()
    documentacion_requerida = models.TextField()
    consideraciones_finales = models.TextField()

    def __str__(self):
        return f"Gastos {self.direccion} - {self.parte}"

from django.db import models

from django.db import models

class ReservaCompraData(models.Model):
    nombre_inmobiliaria = models.CharField(max_length=255)
    matricula = models.CharField(max_length=100)
    nombre_apellido_corredor = models.CharField(max_length=255)
    dni = models.CharField(max_length=20)
    nombre_reservante = models.CharField(max_length=255)
    apellido_reservante = models.CharField(max_length=255)
    direccion_reservante = models.CharField(max_length=255)
    dni_reservante = models.CharField(max_length=20)
    email_reservante = models.EmailField()
    direccion_inmueble = models.CharField(max_length=255)
    matricula_inmueble = models.CharField(max_length=100)
    dgr = models.CharField(max_length=255, blank=True, null=True)
    suma_letras = models.CharField(max_length=255)
    suma_numeros = models.DecimalField(max_digits=10, decimal_places=2)
    monto_oferta_letras = models.CharField(max_length=255)
    monto_oferta_numeros = models.DecimalField(max_digits=10, decimal_places=2)
    condicion_iti = models.CharField(max_length=255)
    condicion_escritura = models.CharField(max_length=255)
    documentacion_exhibida = models.TextField()
    plazo_reserva = models.CharField(max_length=255)
    propiedad_entrega = models.CharField(max_length=255)
    plazo_reserva_letras = models.CharField(max_length=255)
    plazo_reserva_numeros = models.CharField(max_length=255)
    domicilio_inmobiliaria = models.CharField(max_length=255)
    total_honorarios_dinero = models.DecimalField(max_digits=10, decimal_places=2)
    porcentaje_honorarios_parte = models.DecimalField(max_digits=5, decimal_places=2)
    valor_honorarios_parte_compradora = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_inmobiliaria_colega = models.CharField(max_length=255, blank=True, null=True)
    corredor_colega = models.CharField(max_length=255, blank=True, null=True)
    matricula_colega = models.CharField(max_length=100, blank=True, null=True)
    honorarios_colega_porcentaje = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    total_honorarios_dinero_colega = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Reserva Compra {self.nombre_reservante} - {self.dni_reservante}"
