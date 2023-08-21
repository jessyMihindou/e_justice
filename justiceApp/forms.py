from django import forms
from .models import Demande


class DemandeFormEtranger(forms.ModelForm):
    class Meta:
        model = Demande
        fields = ['fichier_document_identite', 'lieu_naissance', 'date_naissance', 'adresse', 'code_postal', 'ville',
                  'pays', 'justificatif_domicile']


class DemandeFormGabonais(forms.ModelForm):
    class Meta:
        model = Demande
        fields = ['fichier_document_identite', 'lieu_naissance', 'date_naissance', 'adresse', 'code_postal', 'ville','pays',
                  'justificatif_domicile']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pays'].initial = 'Gabon'
        self.fields['pays'].widget.attrs['readonly'] = True



class DemanndeFormAdmin(forms.ModelForm):
    class Meta:
        model = Demande
        fields = ['fichier_document_identite',
                  'lieu_naissance', 'date_naissance', 'adresse', 'code_postal','ville', 'pays', 'justificatif_domicile','statut']
