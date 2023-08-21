"""
URL configuration for e_justice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from justiceApp import views
import Authentication.views
from Authentication.models import User
from justiceApp.models import Demande

from django.contrib import admin



from django.contrib import admin


class DemandeAdmin(admin.ModelAdmin):
    list_display = ('numero_de_demande', 'utilisateur', 'date_creation', 'statut', 'type_document_identite', 'fichier_document_identite', 'lieu_naissance', 'date_naissance', 'adresse', 'code_postal', 'ville', 'pays', 'justificatif_domicile')


admin.site.register(Demande, DemandeAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'telephone', 'nationalite', 'role')


admin.site.register(User, UserAdmin)

urlpatterns = [
    path('', Authentication.views.login_page, name='login'),
    path('signup/', Authentication.views.signup_page, name='signup'),
    path('index/', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('logout', Authentication.views.logout_user, name='logout'),
    path('gabonais/', views.citoyen_gabon_registry, name='citoyen_gabonais'),
    path('etranger/', views.citoyen_etranger_registry, name='citoyen_etranger'),
    path('detail/',views.demande_detail, name='demande_detail'),
    path('admin_page/', Authentication.views.admin_page, name='admin_page'),
    path('admin_page/user/<str:telephone>/update/', Authentication.views.user_update, name='user_update'),
    path('admin_page/user/<str:telephone>/delete/', Authentication.views.user_delete, name='user_delete'),
    path('demande/<str:telephone>/update/', Authentication.views.user_demande_update, name='user_demande_update'),
    path('demande/<str:telephone>/delete/', Authentication.views.user_demande_delete, name='user_demande_delete'),

]


