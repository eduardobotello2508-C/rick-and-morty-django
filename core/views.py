from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .models import Character
from .forms import CharacterForm

# 1. READ & FILTERS: Disponible para cualquier usuario autenticado (Admin o Editor)
@login_required
def character_list(request):
    characters = Character.objects.all().order_by('id')

    name_query = request.GET.get('name')
    status_query = request.GET.get('status')
    species_query = request.GET.get('species')
    gender_query = request.GET.get('gender')

    if name_query:
        characters = characters.filter(name__icontains=name_query)
    if status_query:
        characters = characters.filter(status__iexact=status_query)
    if species_query:
        characters = characters.filter(species__icontains=species_query)
    if gender_query:
        characters = characters.filter(gender__iexact=gender_query)

    paginator = Paginator(characters, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Verificamos si el usuario tiene permiso para modificar datos
    can_edit = request.user.has_perm('core.change_character')

    context = {
        'page_obj': page_obj,
        'can_edit': can_edit,
        'name_query': name_query or '',
        'status_query': status_query or '',
        'species_query': species_query or '',
        'gender_query': gender_query or '',
    }
    return render(request, 'core/character_list.html', context)

# 2. CREATE: Solo usuarios con permiso de creación
@login_required
@permission_required('core.add_character', raise_exception=True)
def character_create(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Personaje creado correctamente!')
            return redirect('character_list')
    else:
        form = CharacterForm()
    return render(request, 'core/character_form.html', {'form': form, 'action': 'Crear'})

# 3. UPDATE: Solo usuarios con permiso de edición
@login_required
@permission_required('core.change_character', raise_exception=True)
def character_update(request, pk):
    character = get_object_or_404(Character, pk=pk)
    if request.method == 'POST':
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Personaje actualizado correctamente!')
            return redirect('character_list')
    else:
        form = CharacterForm(instance=character)
    return render(request, 'core/character_form.html', {'form': form, 'action': 'Editar', 'character': character})

# 4. DELETE: Solo usuarios con permiso de eliminación
@login_required
@permission_required('core.delete_character', raise_exception=True)
def character_delete(request, pk):
    character = get_object_or_404(Character, pk=pk)
    if request.method == 'POST':
        character.delete()
        messages.success(request, '¡Personaje eliminado con éxito!')
        return redirect('character_list')
    return render(request, 'core/character_confirm_delete.html', {'character': character})