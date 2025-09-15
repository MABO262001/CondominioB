import backend.models.seeders.rol_seeders
from backend.models.seeders.rol_seeders import seed_roles
from backend.models.seeders.user_seeders import seed_users

def run_all_seeders():
    print("Ejecutando Seeders.......")
    seed_roles()
    seed_users()

    print("Seeders ejecutados con éxito")