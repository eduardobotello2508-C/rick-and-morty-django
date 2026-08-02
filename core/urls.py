from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Lectura y Filtros
    path('', views.character_list, name='character_list'),
    
    # Operaciones CRUD
    path('character/create/', views.character_create, name='character_create'),
    path('character/<int:pk>/edit/', views.character_update, name='character_update'),
    path('character/<int:pk>/delete/', views.character_delete, name='character_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]