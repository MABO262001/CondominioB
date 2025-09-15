from backend.models.users_model import User
from backend.models.rol_model import Rol
from django.contrib.auth.hashers import make_password

def seed_users():
    users_data = [
        {"name": "MABO262001", "email": "ballivian02@gmail.com", "password": "123456789", "status": True, "url_foto": None, "rol": "Master"},
        {"name": "Usuario2", "email": "empleado@gmail.com", "password": "123456789", "status": True, "url_foto": None, "rol": "Empleado"},
        {"name": "Usuario3", "email": "usuario3@example.com", "password": "password123", "status": True, "url_foto":None, "rol": "Cliente"},
    ]

    for user_data in users_data:
        if not User.objects.filter(email=user_data["email"]).exists():
            user_data["password"] = make_password(user_data["password"])
            user_data["rol"] = Rol.objects.get(name=user_data["rol"])
            User.objects.create(**user_data)
    print(f'Seeder "{User.__name__}" ejecutado con éxito.')