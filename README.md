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
- Activar el entorno virtual
 ``` python -m venv venv```
- Entrar a la ruta del proyecto y ingresar al CMD o PowerShell
- Introduccir siguiente comando
 ```.\venv\Scripts\Activate.ps1```
- Ingresar el siguente comando opcional que se utiliza para darle permisos en caso de que windows no te permita
```Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass```
- Instalar las dependencias
```pip install django pymysql requests```

3. **Usar MySQL Workbench o phpMyAdmin**
- Si tienes instalado MySQL Workbench:

- Ábrelo y haz doble clic en tu conexión Local instance MySQL.

- Pón tu contraseña.

- En la pestaña de SQL escribe:

```CREATE DATABASE IF NOT EXISTS rick_db;```

- y dale al rayo para ejecutar.

4. **Ejecutar migraciones y sincronizar datos:**
   
- Ejecuta las migraciones estructurales de Django y descarga los datos de la AP

- Abrir una terminal en visual

- colocar la ruta de donde tienes guardado tu proyecto

- Ingresar el siguente comando opcional que se utiliza para darle permisos en caso de que windows no te permita

```Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass```

- Colocar el siguente comando

```.\venv\Scripts\Activate.ps1```

- Una vez activado el entorno virtual en visual se utilizara los siguente comandos para las migraciones de la base de datos

- Aplicar migraciones iniciales de la BD

```python manage.py migrate```

- Sincronizar datos desde la API oficial de Rick & Morty

```python manage.py sync_api```

- En caso de que falle las migraciones por usuario o contraseña

- Ingresar a la carpeta rick_project dentro de visual y buscar el archivo settings.py para modificar las credenciales de usuario y contraseña

5. **Iniciar servidor:**
- Levanta la aplicación para verla en tu navegador:

```python manage.py runserver```

- Abre tu navegador web y entra a:

```http://127.0.0.1:8000/```
