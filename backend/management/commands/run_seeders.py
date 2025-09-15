# backend/management/commands/run_seeders.py
from django.core.management.base import BaseCommand
from backend.models.seeders.seeders import run_all_seeders

class Command(BaseCommand):
    help = 'Ejecuta todos los seeders'

    def handle(self, *args, **kwargs):
        run_all_seeders()