# 🛸 Rick & Morty Django Portal

Proyecto desarrollado en **Django** y **MySQL** que consume la API pública de Rick & Morty, gestiona personajes de forma relacional y ofrece control de acceso basado en roles (RBAC).

## 🚀 Características Principales

- **Base de Datos Relacional:** Configurada en MySQL para gestionar personajes, ubicaciones y episodios con relaciones `ForeignKey` y `ManyToManyField`.
- **Sincronización Automatizada:** Comando personalizado de Django (`python manage.py sync_api`) para importar y actualizar +200 personajes desde la API pública sin duplicar registros.
- **Gestión de Permisos (RBAC):**
  - **Administrador:** Acceso total (CRUD de personajes + sincronización).
  - **Editor:** Permiso de solo lectura y uso de filtros.
- **Búsqueda y Filtros:** Filtrado dinámico por nombre, estado, especie y género con paginación.
- **Interfaz Web:** Diseño oscuro/neón temático con Bootstrap 5 y modales interactivos de confirmación para eliminación.

## 🛠️ Tecnologías Utilizadas

- Python 3.14 / Django 6
- MySQL / PyMySQL
- Bootstrap 5
- Git / GitHub

## ⚙️ Instalación y Ejecución Local

1. **Clonar repositorio:**
   ```bash
   git clone https://github.com/eduardobotello2508-C/rick-and-morty-django.git

2. **Activar entorno virtual e instalar dependencias:**
- .\venv\Scripts\Activate.ps1
- pip install django pymysql requests

3. **Ejecutar migraciones y sincronizar datos:**

- python manage.py migrate
- python manage.py sync_api

4. **Iniciar servidor:**
- python manage.py runserver

---

### 📤 Para subir la versión final a GitHub:

En tu terminal ejecuta:

```powershell
git add .
git commit -m "docs: Actualizar README.md principal"
git push origin main
