# Authentication/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, telephone, password=None, **extra_fields):
        if not telephone:
            raise ValueError('The Phone number must be set')
        user = self.model(telephone=telephone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, telephone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(telephone, password, **extra_fields)

class User(AbstractUser):
    ETRANGER = 'etranger'
    GABON = 'gabon'
    STANDARD_USER = 'STANDARD_USER'
    ADMIN = 'ADMIN'

    ROLE_CHOICES = (
        (STANDARD_USER, 'Utilisateur standard'),
        (ADMIN, 'Administrateur'),
    )

    NATIONALITE_CHOICES = [
        ('etranger', 'Étranger'),
        ('gabon', 'Gabonais'),
    ]

    username = None
    nom = models.CharField(max_length=30, blank=True, verbose_name="Prénom", default='')
    prenom = models.CharField(max_length=30, blank=True, verbose_name="Nom de famille", default='')
    telephone = models.CharField(max_length=20, unique=True, blank=True, default='')
    nationalite = models.CharField(max_length=20, choices=NATIONALITE_CHOICES, default='')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=STANDARD_USER)

    USERNAME_FIELD = 'telephone'

    objects = CustomUserManager()

    def __str__(self):
        return self.telephone
