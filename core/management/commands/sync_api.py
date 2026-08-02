import requests
from django.core.management.base import BaseCommand
from core.models import Character, Location, Episode

class Command(BaseCommand):
    help = 'Sincroniza personajes, ubicaciones y episodios desde la API de Rick and Morty'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Iniciando sincronización con la API...'))
        
        target_characters = 200
        synced_characters = 0
        page = 1

        while synced_characters < target_characters:
            url = f'https://rickandmortyapi.com/api/character?page={page}'
            response = requests.get(url)
            
            if response.status_code != 200:
                self.stdout.write(self.style.ERROR('Error al conectar con la API.'))
                break

            data = response.json()
            results = data.get('results', [])

            for char_data in results:
                if synced_characters >= target_characters:
                    break

                # 1. Obtener/Crear Ubicación de Origen
                origin_obj = None
                origin_name = char_data['origin']['name']
                if origin_name and origin_name != 'unknown':
                    origin_obj, _ = Location.objects.get_or_create(
                        name=origin_name,
                        defaults={'type': 'Desconocido', 'dimension': 'Desconocida'}
                    )

                # 2. Obtener/Crear Ubicación Actual
                location_obj = None
                loc_name = char_data['location']['name']
                if loc_name and loc_name != 'unknown':
                    location_obj, _ = Location.objects.get_or_create(
                        name=loc_name,
                        defaults={'type': 'Desconocido', 'dimension': 'Desconocida'}
                    )

                # 3. Crear o Actualizar el Personaje
                character, created = Character.objects.update_or_create(
                    id=char_data['id'],
                    defaults={
                        'name': char_data['name'],
                        'status': char_data['status'],
                        'species': char_data['species'],
                        'type': char_data['type'],
                        'gender': char_data['gender'],
                        'image': char_data['image'],
                        'origin': origin_obj,
                        'location': location_obj,
                    }
                )

                # 4. Procesar Episodios de forma segura (sin saturar la API)
                for ep_url in char_data['episode']:
                    # Extraer el ID del episodio desde el final de la URL (ej: .../episode/1 -> 1)
                    ep_id = ep_url.split('/')[-1]
                    episode_obj, _ = Episode.objects.get_or_create(
                        id=ep_id,
                        defaults={
                            'name': f'Episodio {ep_id}',
                            'episode': f'EP-{ep_id}',
                            'air_date': 'N/A'
                        }
                    )
                    character.episodes.add(episode_obj)

                synced_characters += 1
                self.stdout.write(f'Sincronizado ({synced_characters}/{target_characters}): {character.name}')

            page += 1

        self.stdout.write(self.style.SUCCESS(f'¡Éxito! Se han sincronizado {synced_characters} personajes correctamente en MySQL.'))