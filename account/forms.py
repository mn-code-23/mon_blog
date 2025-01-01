from django import forms

from account.models import Utilisateur


#Login
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nom d\'utilisateur'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Mot de passe'
    }))

#Profil
class Profil(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'photo_profil', 'site_web']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Prenom'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Adresse email'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Saisir votre bio ici .....',
                'rows': 4
            }),
            'photo_profil': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id': 'formFile'
            }),
            'site_web': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre site web si vous en avez'
            }),
        }