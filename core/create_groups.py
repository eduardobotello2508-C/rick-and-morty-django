import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rick_project.settings')
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from core.models import Character

def create_roles():
    # 1. Crear Grupos
    admin_group, _ = Group.objects.get_or_create(name='Administrador')
    editor_group, _ = Group.objects.get_or_create(name='Editor')

    # 2. Obtener permisos del modelo Character
    content_type = ContentType.objects.get_for_model(Character)
    char_permissions = Permission.objects.filter(content_type=content_type)

    # 3. Asignar permisos
    # Administrador: Todos los permisos (add, change, delete, view)
    admin_group.permissions.set(char_permissions)

    # Editor: Solo permiso de lectura (view)
    view_perm = Permission.objects.get(codename='view_character', content_type=content_type)
    editor_group.permissions.set([view_perm])

    print("¡Grupos 'Administrador' y 'Editor' creados e integrados exitosamente!")

if __name__ == '__main__':
    create_roles()