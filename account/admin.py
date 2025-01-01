# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur
# from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = Utilisateur

    # Personnalisation de l'affichage dans l'admin
    # list_display = ['username', 'email', 'date_naissance', 'is_staff']

    # Ajout des champs personnalisés dans l'interface d'admin
    fieldsets = UserAdmin.fieldsets + (
        ('Informations supplémentaires', {
            'fields': ('bio', 'photo_profil', 'site_web')
        }),
    )


admin.site.register(Utilisateur, CustomUserAdmin)