from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, serializers
from backend.models.users_model import User
from backend.models.rol_model import Rol
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.db.models import Q

# ========================
# SERIALIZADOR
# ========================

class UserSerializer(serializers.ModelSerializer):
    rol = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'status', 'rol']

# ========================
# ENDPOINTS DE USUARIO
# ========================

# GET http://localhost:8000/api/usuarios/
@api_view(['GET'])
def listar_usuarios(request):
    try:
        usuarios = User.objects.select_related('rol', 'user').all()

        if not usuarios.exists():
            return response_error("No existen usuarios registrados.", status.HTTP_404_NOT_FOUND)

        data = UserSerializer(usuarios, many=True).data
        return response_ok("Usuarios obtenidos correctamente", data)

    except Exception as e:
        return response_error(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)

# GET http://localhost:8000/api/usuarios/{id}/
@api_view(['GET'])
def obtener_usuario(request, id):
    try:
        usuario = User.objects.select_related('rol', 'user').get(pk=id)
        data = UserSerializer(usuario).data
        return response_ok("Usuario obtenido correctamente", data)

    except User.DoesNotExist:
        return response_error("Usuario no encontrado", status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return response_error(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)

# POST http://localhost:8000/api/usuarios/crear/
@api_view(['POST'])
def crear_usuario(request):
    try:
        data = request.data

        if User.objects.filter(Q(email=data.get('email')) | Q(name=data.get('name'))).exists():
            return response_error("Ya existe un usuario con ese nombre o correo electrónico")

        rol_id = data.get('rol_id')
        if not rol_id:
            return response_error("Falta el campo 'rol_id'")

        rol = Rol.objects.get(pk=rol_id)

        user = User(
            name=data.get('name'),
            email=data.get('email'),
            password=make_password(data.get('password')),
            url_foto=data.get('url_foto', ''),
            status=data.get('status', True),
            user_id=data.get('user_id'),
            rol=rol
        )
        user.full_clean()
        user.save()
        return response_ok("Usuario creado correctamente", {"id": user.id})

    except Rol.DoesNotExist:
        return response_error("Rol no encontrado")
    except ValidationError as e:
        return response_error(e.message_dict)
    except Exception as e:
        return response_error(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)

# PUT http://localhost:8000/api/usuarios/actualizar/{id}/
@api_view(['PUT'])
def actualizar_usuario(request, id):
    try:
        data = request.data
        user = User.objects.get(pk=id)

        user.name = data['name']
        user.email = data['email']
        user.status = data['status']
        user.url_foto = data.get('url_foto', '')
        user.user_id = data.get('user_id')
        user.rol = Rol.objects.get(pk=data['rol_id'])

        user.full_clean()
        user.save()
        return response_ok("Usuario actualizado correctamente")

    except User.DoesNotExist:
        return response_error("Usuario no encontrado", status.HTTP_404_NOT_FOUND)
    except Rol.DoesNotExist:
        return response_error("Rol no encontrado", status.HTTP_404_NOT_FOUND)
    except ValidationError as e:
        return response_error(e.message_dict)
    except Exception as e:
        return response_error(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)

# DELETE http://localhost:8000/api/usuarios/eliminar/{id}/
@api_view(['DELETE'])
def eliminar_usuario(request, id):
    try:
        user = User.objects.get(pk=id)
        user.status = False
        user.save()
        return response_ok("Usuario desactivado correctamente")

    except User.DoesNotExist:
        return response_error("Usuario no encontrado", status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return response_error(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)

# ========================
# FUNCIONES AUXILIARES
# ========================

def response_ok(message, data=None):
    return Response({"success": True, "message": message, "data": data}, status=status.HTTP_200_OK)

def response_error(message, code=status.HTTP_400_BAD_REQUEST):
    return Response({"success": False, "error": message}, status=code)
