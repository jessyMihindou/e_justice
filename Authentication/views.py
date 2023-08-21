# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from justiceApp.forms import DemanndeFormAdmin
from justiceApp.models import Demande
from . import forms
from django.contrib.auth import login, authenticate, logout  # import des fonctions login et authenticate
from Authentication.models import User
from .forms import LoginForm, UserForm
from django.contrib import messages


def logout_user(request):
    logout(request)
    return redirect('login')


def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                print(user.role)
                print(User.ADMIN)
                if user.role == User.ADMIN:
                    return redirect('admin_page')
                elif user.nationalite == User.ETRANGER:
                    return redirect('citoyen_etranger')
                elif user.nationalite == User.GABON:
                    return redirect('citoyen_gabonais')
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'Authentication/login.html', context={'form': form, 'message': message})


@login_required
def admin_page(request):
    users = User.objects.filter(role=User.STANDARD_USER)
    demandes = Demande.objects.all()
    return render(request, 'Authentication/admin_page.html', {'users': users, 'user': request.user, 'demandes': demandes })


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect('login')
    return render(request, 'Authentication/signup.html', context={'form': form})


@login_required
def user_update(request, telephone):
    # Récupérez l'objet User correspondant au numéro de téléphone
    user = get_object_or_404(User, telephone=telephone)
    # Créez un formulaire pour mettre à jour les informations de l'utilisateur
    form = UserForm(request.POST or None, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully.')
            return redirect('admin_page')
    return render(request, 'Authentication/user_update.html', {'form': form, 'user': user})


@login_required
def user_delete(request, telephone):
    # Récupérez l'objet User correspondant au numéro de téléphone
    user = get_object_or_404(User, telephone=telephone)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully.')
        return redirect('admin_page')
    return render(request, 'Authentication/user_delete.html', {'object': user, 'user': user})


@login_required
def user_demande_update(request, telephone):
    # Récupérez l'objet User correspondant au numéro de téléphone
    user = get_object_or_404(User, telephone=telephone)
    # Récupérez l'objet Demande associé à l'utilisateur
    demande = get_object_or_404(Demande, utilisateur=user)
    # Créez un formulaire pour mettre à jour les informations de la demande
    form = DemanndeFormAdmin(request.POST or None, instance=demande)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Demande mise à jour avec succès.')
            return redirect('admin_page')
    return render(request, 'Authentication/user_demande_update.html', {'form': form, 'user': user, 'demande': demande})

@login_required
def user_demande_delete(request, telephone):
    # Récupérez l'objet User correspondant au numéro de téléphone
    user = get_object_or_404(User, telephone=telephone)
    # Récupérez l'objet Demande associé à l'utilisateur
    demande = get_object_or_404(Demande, utilisateur=user)
    if request.method == 'POST':
        demande.delete()
        messages.success(request, 'Demande supprimée avec succès.')
        return redirect('admin_page')
    return render(request, 'Authentication/user_demande_delete.html', {'object': demande, 'user': user})
