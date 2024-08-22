from django import forms

class ContractForm(forms.Form):
    ciudad = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese la ciudad'})
    )
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text='Ingrese la fecha del contrato en formato AAAA-MM-DD.'
    )
    locador_nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del locador'})
    )
    locador_dni = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el DNI del locador'})
    )
    telefono_locador = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el teléfono del locador'})
    )
    mail_locador = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Ingrese el correo electrónico del locador'})
    )
    nacionalidad_locador = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese la nacionalidad del locador'})
    )
    locador_direccion = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese la dirección del locador'})
    )
    ciudaddondevive_locador = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese la ciudad donde vive el locador'})
    )
    provincia_locador = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese la provincia del locador'})
    )
    locatario_nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del locatario'})
    )
    locatario_dni = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el DNI del locatario'})
    )
    mail_locatario = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Ingrese el correo electrónico del locatario'})
    )
    telefono_locatario = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el teléfono del locatario'})
    )
    superficie_inmueble = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese la superficie del inmueble'})
    )
    direccion_inmueble = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese la dirección del inmueble'})
    )
    colorcasa = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el color de la casa'})
    )
    tipo_pintura = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el tipo de pintura'})
    )
    marca_pintura = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese la marca de pintura'})
    )
    caracteristicas = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Ingrese las características del inmueble'})
    )
    alquiler_mensual = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder': 'Ingrese el canon locativo en números'})
    )
    aumento = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el aumento mensual y detalle del índice'})
    )
    meses = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'Ingrese el número de meses'})
    )
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Formato: DD/MM/YYYY'}),
        help_text='Ingrese la fecha de inicio del contrato en formato DD/MM/AAAA.'
    )
    fecha_fin = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Formato: DD/MM/YYYY'}),
        help_text='Ingrese la fecha de fin del contrato en formato DD/MM/AAAA.'
    )
    garantias = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 10,
            'placeholder': 'Ingrese las garantías, detalles de los fiadores, nombres completos, domicilios y datos personales.'
        })
    )
    
from django import forms

class GastosForm(forms.Form):
    direccion = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese la dirección'})
    )
    parte = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese la parte'})
    )
    tipo_operacion = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el tipo de operación'})
    )
    pago_contado = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder': 'Ingrese el pago contado'})
    )
    financiacion = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder': 'Ingrese la financiación'})
    )
    honorarios = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder': 'Ingrese los honorarios'})
    )
    condiciones = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Ingrese las condiciones'})
    )
    documentacion_requerida = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Ingrese la documentación requerida'})
    )
    consideraciones_finales = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Ingrese las consideraciones finales'})
    )


from django import forms

from django import forms

class ReservaCompraForm(forms.Form):
    nombre_inmobiliaria = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el nombre de la inmobiliaria'})
    )
    matricula = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese la matrícula'})
    )
    nombre_apellido_corredor = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el nombre y apellido del corredor'})
    )
    dni = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el DNI'})
    )
    nombre_reservante = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del reservante'})
    )
    apellido_reservante = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el apellido del reservante'})
    )
    direccion_reservante = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese la dirección del reservante'})
    )
    dni_reservante = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el DNI del reservante'})
    )
    email_reservante = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Ingrese el e-mail del reservante'})
    )
    direccion_inmueble = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese la dirección del inmueble'})
    )
    matricula_inmueble = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese la matrícula del inmueble'})
    )
    dgr = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese DGR (dato no obligatorio)'})
    )
    suma_letras = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese la RESERVA en letras'})
    )
    suma_numeros = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder': 'Ingrese la RESERVA en números'})
    )
    monto_oferta_letras = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el monto de la oferta en letras'})
    )
    monto_oferta_numeros = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder': 'Ingrese el monto de la oferta en números'})
    )
    condicion_iti = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese la condición ITI (corresponde o no)'})
    )
    condicion_escritura = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese la condición de escritura'})
    )
    documentacion_exhibida = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Ingrese la documentación exhibida'})
    )
    plazo_reserva = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el plazo de reserva (letras, números o fecha)'})
    )
    propiedad_entrega = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese la propiedad se entrega (libre de ocupantes, alquilada, otros)'})
    )
    plazo_reserva_letras = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el plazo de reserva en letras'})
    )
    plazo_reserva_numeros = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el plazo de reserva en números'})
    )
    domicilio_inmobiliaria = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el domicilio de la inmobiliaria (dirección, barrio, localidad, provincia)'})
    )
    total_honorarios_dinero = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder': 'Ingrese el total de honorarios en dinero'})
    )
    porcentaje_honorarios_parte = forms.DecimalField(
        max_digits=5,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder': 'Ingrese el porcentaje de honorarios para cada parte'})
    )
    valor_honorarios_parte_compradora = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder': 'Ingrese el valor de los honorarios para la parte compradora'})
    )
    nombre_inmobiliaria_colega = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el nombre de la inmobiliaria colega (si no existe, colocar sus datos)'})
    )
    corredor_colega = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el corredor colega (si no existe, colocar sus datos)'})
    )
    matricula_colega = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese la matrícula del colega (si no existe, colocar sus datos)'})
    )
    honorarios_colega_porcentaje = forms.DecimalField(
        max_digits=5,
        decimal_places=2,
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Ingrese el porcentaje de honorarios del colega (si no existe, colocar sus datos)'})
    )
    total_honorarios_dinero_colega = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Ingrese el total de honorarios en dinero del colega (si no existe, colocar sus datos)'})
    )
