# urls.py (en la carpeta del proyecto)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasador.urls')),  # Incluye las URLs de la aplicación
]
