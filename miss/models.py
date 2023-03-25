from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import F
# Create your models here.


class Candidate(models.Model):

    prenom = models.CharField(max_length=140, blank=True)
    nom = models.CharField(max_length=140, blank=True)
    numero = models.IntegerField(default=0)
    nombreVote = models.IntegerField(default=0, editable = False)
    profile_image = models.ImageField(upload_to = 'media', null = True, blank = True)
    age = models.IntegerField(default=0)
    projet = models.TextField(blank=True)

    def __str__(self):
        return self.nom

class Candidat(models.Model):

    prenom = models.CharField(max_length=140, blank=True)
    nom = models.CharField(max_length=140, blank=True)
    numero = models.IntegerField(default=0)
    nombreVote = models.IntegerField(default=0, editable = False)
    profile_image = models.ImageField(upload_to = 'media', null = True, blank = True)
    age = models.IntegerField(default=0)
    projet = models.TextField(blank=True)

    def __str__(self):
        return self.nom

class Actualites(models.Model):

    titre = models.CharField(max_length=140, blank=True)
    profile_image = models.ImageField(upload_to = 'media', null = True, blank = True)
    description = models.TextField(blank=True)
    auteur = models.CharField(max_length=140, blank=True)
    date = models.DateField(auto_now_add = True, null = True)

class Souscription(models.Model):

    payment_ref = models.CharField(max_length=140, blank=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.PROTECT, null = True, blank =True)
    candidat = models.ForeignKey(Candidat, on_delete=models.PROTECT, null = True, blank =True)
    nbVote = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add = True)
    nom = models.CharField(max_length=140, blank=True)
    telephone = models.CharField(max_length=140, blank=True)



class Transaction(models.Model):
    payment_ref = models.CharField(default='', max_length=100)
    ref_bsend  = models.CharField(default='', max_length=100)
    date  = models.DateTimeField(auto_now_add = True)
    statut  = models.CharField(default='', null = True, max_length=100)


class Notification(models.Model):
    email = models.CharField(default='', max_length=100)
    message  = models.CharField(default='', max_length=100)
    date  = models.DateTimeField(auto_now_add = True)

@receiver(post_save, sender = Transaction)
def push_nb(sender, instance, created, **kwargs):
    if created:
        # print(g)
        if instance.statut ==  "sucess":
            souscription = Souscription.objects.get(payment_ref = instance.payment_ref)

            if souscription.candidate is None:
                user = Candidat.objects.get(id = souscription.candidat.id)

                user.nombreVote = F('nombreVote')+souscription.nbVote
                user.save()
            else:
                user = Candidate.objects.get(id = souscription.candidate.id)

                user.nombreVote = F('nombreVote')+souscription.nbVote
                user.save()




