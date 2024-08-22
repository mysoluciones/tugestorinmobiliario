# Generated by Django 5.0.2 on 2024-08-18 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('DEPARTAMENTO', 'Departamento'), ('CASA', 'Casa'), ('LOTE', 'Lote')], max_length=20)),
                ('direccion', models.CharField(max_length=255)),
                ('comentarios', models.TextField(blank=True)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
