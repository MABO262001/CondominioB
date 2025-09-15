#backend/models/users_model.py
from django.db import models
from backend.models.rol_model import Rol

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    url_foto = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    user = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='related_users')

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.name