# authentication/forms.py
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from Authentication.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label='Nom d’utilisateur', widget=forms.TextInput(attrs={'value': ''}))
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'username'






class SignupForm(UserCreationForm):
    nationalite = forms.ChoiceField(choices=User.NATIONALITE_CHOICES, required=True)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['nom', 'prenom', 'telephone', 'nationalite']

    def clean_numero_de_telephone(self):
        telephone = self.cleaned_data['telephone']
        if get_user_model().objects.filter(telephone=telephone).exists():
            raise forms.ValidationError('Ce numéro de téléphone est déjà pris.')
        return telephone



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nom', 'prenom', 'telephone', 'nationalite', 'role']
