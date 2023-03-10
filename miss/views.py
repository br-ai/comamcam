from django.shortcuts import render
from .models import Candidate

# Create your views here.
def home(request):
    candidates = Candidate.objects.all().order_by('?')
    candidatesOr = Candidate.objects.all().order_by('-nombreVote')
    return render(request, 'index.html', {'candidates': candidates, 'candidatesor': candidatesOr, 'i':0})