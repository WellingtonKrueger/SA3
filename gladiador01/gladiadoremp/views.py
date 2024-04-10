from django.shortcuts import render
from django.views.generic import DateDetailView

def index(request):
    return render(request, "partial/home.html")

def elenco(request):
    return render(request, "partial/elenco.html")

def enredo(request):
    return render(request, "partial/enredo.html")
