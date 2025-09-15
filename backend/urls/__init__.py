# backend/urls/init__.py
from django.urls import path, include
from backend.urls import routes

urlpatterns = [
    *routes.urlpatterns,   # expone las rutas Laravel-style
]
