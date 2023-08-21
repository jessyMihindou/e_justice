from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from Authentication.models import User
from .forms import DemandeFormEtranger, DemandeFormGabonais
from .models import Demande


@login_required
def index(request):
    user = request.user  # Récupère l'utilisateur connecté
    return render(request, 'justiceApp/index.html', {'user': user})  # Passe l'utilisateur au template

@login_required
def citoyen_etranger_registry(request):
    # Check if the user has already made a request
    if Demande.objects.filter(utilisateur=request.user).exists():
        return redirect('demande_detail')
    if request.method == 'POST':
        form = DemandeFormEtranger(request.POST, request.FILES)
        if form.is_valid():
            demande = form.save(commit=False)
            demande.utilisateur = request.user
            demande.nationalite = 'etranger'
            demande.type_document_identite = 'passport'
            demande.save()
            return redirect('demande_detail')
    else:
        form = DemandeFormEtranger()
    return render(request, 'justiceApp/citoyen_etranger_registry.html', {'form': form})

@login_required
def citoyen_gabon_registry(request):
    # Check if the user has already made a request
    if Demande.objects.filter(utilisateur=request.user).exists():
        return redirect('demande_detail')
    if request.method == 'POST':
        form = DemandeFormGabonais(request.POST, request.FILES)
        if form.is_valid():
            demande = form.save(commit=False)
            demande.utilisateur = request.user
            demande.nationalite = 'gabonais'
            demande.type_document_identite = 'acte_naissance'
            demande.save()
            return redirect('demande_detail')
    else:
        form = DemandeFormGabonais()
    return render(request, 'justiceApp/citoyen_gabon_registry.html', {'form': form})


@login_required
def demande_detail(request):
    demandes = Demande.objects.filter(utilisateur=request.user)
    if demandes:
        demande = demandes[0]
    else:
        demande = None
    return render(request, 'justiceApp/demande_detail.html', {'demande': demande})
