# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class Utilisateur(AbstractUser):
    # Champs par défaut hérités de AbstractUser:
    # username, email, first_name, last_name, password, etc.

    # Ajout de champs personnalisés
    bio = models.TextField(max_length=500, blank=True)
    photo_profil = models.ImageField(upload_to="profils", blank=True, null=True)
    # date_naissance = models.DateField(null=True, blank=True)
    site_web = models.URLField(max_length=200, blank=True)
    # telephone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username