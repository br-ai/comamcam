from django.shortcuts import render, redirect
from .models import Candidate, Souscription, Transaction, Candidat, Actualites, Notification
from .serializers import TransactionSerializer
import string
import random
import requests
import json
from rest_framework import viewsets
from django.db.models import F
from django.http import HttpResponse

# Create your views here.
def home(request):
    actualites = Actualites.objects.all()
    candidates = Candidate.objects.all().order_by('?')
    candidatesOr = Candidate.objects.all().order_by('-nombreVote')
    candidats = Candidat.objects.all().order_by('?')
    candidatsOr = Candidat.objects.all().order_by('-nombreVote')
    return render(request, 'index.html', {'candidates': candidates, 'candidatesor': candidatesOr, 'candidats': candidats, 'candidatsor': candidatsOr, 'actualites':actualites,})


def allCandidate(request):
    candidates = Candidate.objects.all().order_by('?')
    return render(request, 'allCandidate.html', {'candidates': candidates,})

def candidateDetail(request, numero):
    candidate = Candidate.objects.get(numero = numero)
    return render(request, 'votez.html', {'candidate': candidate,})


def allCandidat(request):
    candidats = Candidat.objects.all().order_by('?')
    return render(request, 'allCandidat.html', {'candidats': candidats,})

def candidatDetail(request, numero):
    candidat = Candidat.objects.get(numero = numero)
    return render(request, 'votezH.html', {'candidat': candidat,})

def galerie(request):
    return render(request, 'galerie.html')

def evenement(request):
    return render(request, 'evenement.html')

def actualite(request, id):
    actualite = Actualites.objects.get(id = id)
    return render(request, 'actualite.html', {'actualite' : actualite})




def votez(request, id):
    nbVote = request.POST['nbVote']
    nom = request.POST['nom']
    telephone = request.POST['telephone']
    S = 10
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
    payment_ref = str(ran)
    candidate = Candidate.objects.get(id = id)
    prix = int(nbVote)
    Souscription.objects.create(payment_ref= payment_ref, candidate = candidate, nbVote = nbVote, nom = nom, telephone = telephone)
    data = {
        'amount' : prix*100,
        'item_ref' : 'Achat parts',
        "amount" : prix*100,
        "phone" : telephone,
        "email" : "test@gmail.com",
        "first_name" : "ras",
        "cmd" : "BS_PAY",
        "currency" : "XAF",
        "description":"Vote pour"+candidate.nom,
        "langue" : "fr",
        "payment_ref" : payment_ref,
        "public_key" : "REF_Ef1cutav9qUhUd0xfdQKSL",
        "country" : "cameroun",
        "country_ccode" : "CM",
        "country_cdial":"237"

    }

    #make a post and return a response in a variable call resp
    resp = requests.post(

        'https://bsend-op.com/api/v1.0/payment/control',
        data=json.dumps(data),
        timeout = 30,
        verify = True,
        headers={"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36", "Content-Type": "application/json"},

    )

    data = resp.json()

    if data['response'] == "Success":
        return redirect(data['payment_url'])
    else:
        return render(request, 'erreur.html', {'message': data['message'],})



def votezH(request, id):
    nbVote = request.POST['nbVote']
    nom = request.POST['nom']
    telephone = request.POST['telephone']
    S = 10
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
    payment_ref = str(ran)
    candidat = Candidat.objects.get(id = id)
    prix = int(nbVote)
    Souscription.objects.create(payment_ref= payment_ref, candidat = candidat, nbVote = nbVote, nom = nom, telephone = telephone)
    data = {
        'amount' : prix*100,
        'item_ref' : 'Achat parts',
        "amount" : prix*100,
        "phone" : telephone,
        "email" : "test@gmail.com",
        "first_name" : "ras",
        "cmd" : "BS_PAY",
        "currency" : "XAF",
        "description":"Vote pour"+candidat.nom,
        "langue" : "fr",
        "payment_ref" : payment_ref,
        "public_key" : "REF_Ef1cutav9qUhUd0xfdQKSL",
        "country" : "cameroun",
        "country_ccode" : "CM",
        "country_cdial":"237"

    }

    #make a post and return a response in a variable call resp
    resp = requests.post(

        'https://bsend-op.com/api/v1.0/payment/control',
        data=json.dumps(data),
        timeout = 30,
        verify = True,
        headers={"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36", "Content-Type": "application/json"},

    )

    data = resp.json()

    if data['response'] == "Success":
        return redirect(data['payment_url'])
    else:
        return render(request, 'erreur.html', {'message': data['message'],})


class TransactionApiView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

def notification(request):
    if request.method == 'POST':
        email = request.POST['email']
        message = request.POST['message']
        Notification.objects.create(email=email, message=message)
        return render(request, 'sucess.html', {'message': 'Merci de nous avoir contacté',})

def sucess(request):
    return render(request, 'sucess.html', {'message': 'Votre vote a été bien enregistré',})

def erreur(request):
    return render(request, 'erreur.html', {'message': 'Malheureusement une erreur est parvenue lors de la demande de vote',})
