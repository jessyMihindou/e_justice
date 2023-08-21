from django.db import models
from Authentication.models import User

class Demande(models.Model):
    STATUT_CHOICES = [
        ('attente', 'En attente'),
        ('traitement', 'En traitement'),
        ('approuvee', 'Approuvée'),
        ('rejetee', 'Rejetée'),
    ]

    DOCUMENT_IDENTITE_CHOICES = [
        ('passport', 'Passeport'),
        ('acte_naissance', 'Acte de naissance'),
    ]

    numero_de_demande = models.AutoField(primary_key=True, unique=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    type_document_identite = models.CharField(max_length=20, choices=DOCUMENT_IDENTITE_CHOICES, default='')

    fichier_document_identite = models.FileField(upload_to='documents/', default='')
    lieu_naissance = models.CharField(max_length=200)
    date_naissance = models.DateField()
    adresse = models.TextField()
    code_postal = models.CharField(max_length=10)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=200)
    justificatif_domicile = models.FileField(upload_to='documents/', default='')
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='attente')

    def formatted_numero_de_demande(self):
        return f"0{self.numero_de_demande:06d}"  # Format pour ajouter des zéros en tête

    def __str__(self):
        return f"{self.formatted_numero_de_demande()} - Demande de casier judiciaire"



