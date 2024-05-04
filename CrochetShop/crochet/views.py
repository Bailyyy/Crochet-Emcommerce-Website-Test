from django.shortcuts import render
from django.http import HttpResponse
from .models import Crochet

def home(request):
    crochet = Crochet.objects.all()
    return render(request, 'home.html', {'crochet': crochet})
                        