from backend.models.rol_model import Rol
from django.db import connection

def seed_roles():
    roles_data = [
        {"name": "Master"},
        {"name": "Administrador"},
        {"name": "Empleado"},
        {"name": "Cliente"},
    ]

    for rol_data in roles_data:
        if not Rol.objects.filter(name=rol_data["name"]).exists():
            Rol.objects.create(name=rol_data["name"])
    print(f'Seeder "{Rol.__name__}" ejecutado con éxito.')