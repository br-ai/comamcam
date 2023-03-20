from django.db import models

# Create your models here.


class Candidate(models.Model):
  
    prenom = models.CharField(max_length=140, blank=True)
    nom = models.CharField(max_length=140, blank=True)
    numero = models.IntegerField(default=0)
    nombreVote = models.IntegerField(default=0, editable = False)
    profile_image = models.ImageField(upload_to = 'media', null = True, blank = True)
    age = models.IntegerField(default=0)
    projet = models.TextField(blank=True)

class Candidat(models.Model):
  
    prenom = models.CharField(max_length=140, blank=True)
    nom = models.CharField(max_length=140, blank=True)
    numero = models.IntegerField(default=0)
    nombreVote = models.IntegerField(default=0, editable = False)
    profile_image = models.ImageField(upload_to = 'media', null = True, blank = True)
    age = models.IntegerField(default=0)
    projet = models.TextField(blank=True)

class Actualites(models.Model):
  
    titre = models.CharField(max_length=140, blank=True)
    profile_image = models.ImageField(upload_to = 'media', null = True, blank = True)
    description = models.TextField(blank=True)
    auteur = models.CharField(max_length=140, blank=True)
    date = models.DateField(auto_now_add = True, null = True)

class Souscription(models.Model):
  
    payment_ref = models.CharField(max_length=140, blank=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.PROTECT, null = True)
    candidat = models.ForeignKey(Candidat, on_delete=models.PROTECT, null = True)
    nbVote = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add = True)
    nom = models.CharField(max_length=140, blank=True)
    telephone = models.CharField(max_length=140, blank=True)



class Transaction(models.Model):
    payment_ref = models.CharField(default='', max_length=100)
    ref_bsend  = models.CharField(default='', max_length=100)
    date  = models.DateTimeField(auto_now_add = True)
    statut  = models.CharField(default='', null = True, max_length=100)

