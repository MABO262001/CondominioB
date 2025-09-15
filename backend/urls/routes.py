# backend/urls/routes.py

from django.urls import path, include
from backend.controllers import UsersController
from backend.urls.config import Route

urlpatterns = []

from backend.controllers import UsersController
from backend.urls.config import Route

urlpatterns = []

urlpatterns += Route(prefix='api/usuarios/',name='usuarios.',controller=UsersController).group([
    ('', 'listar_usuarios', 'listar'),
    ('<int:id>/', 'obtener_usuario', 'detalles'),
    ('crear/', 'crear_usuario', 'crear'),
    ('actualizar/<int:id>/', 'actualizar_usuario', 'actualizar'),
    ('eliminar/<int:id>/', 'eliminar_usuario', 'eliminar'),
])


