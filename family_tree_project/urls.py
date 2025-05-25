# family_tree_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Importa settings para la configuración de MEDIA
from django.conf.urls.static import static # Importa static para servir archivos multimedia
from . import views # Importa las vistas del proyecto principal (para la home)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'), # Página de inicio del proyecto

    # URLs de autenticación de Django (login, logout, password_change, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('users.urls')), # URLs personalizadas de la app de usuarios (registro)

    # URLs de mis aplicaciones
    path('members/', include('family_members.urls')),
    path('stories/', include('family_stories.urls')),
    path('photos/', include('family_photos.urls')),
]

# Sirve archivos multimedia solo en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
