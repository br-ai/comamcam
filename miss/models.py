from django.db import models

# Create your models here.


class Candidate(models.Model):
  
    prenom = models.CharField(max_length=140, blank=True)
    nom = models.CharField(max_length=140, blank=True)
    numero = models.IntegerField(default=0)
    nombreVote = models.IntegerField(default=0)
    profile_image = models.ImageField(upload_to = 'media', null = True, blank = True)