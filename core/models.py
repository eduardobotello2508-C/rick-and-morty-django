from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True, null=True)
    dimension = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class Episode(models.Model):
    name = models.CharField(max_length=255)
    air_date = models.CharField(max_length=255, blank=True, null=True)
    episode = models.CharField(max_length=50) # ej: S01E01

    def __str__(self):
        return f"{self.episode} - {self.name}"

class Character(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=50) # Alive, Dead, unknown
    species = models.CharField(max_length=100)
    type = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=50)
    image = models.URLField(blank=True, null=True)
    
    # Relaciones (1 a Muchos y Muchos a Muchos)
    origin = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, related_name='origin_characters')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, related_name='current_characters')
    episodes = models.ManyToManyField(Episode, related_name='characters')

    def __str__(self):
        return self.name