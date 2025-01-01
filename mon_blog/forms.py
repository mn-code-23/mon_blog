from  django import forms
from .models import Commentaire, Article


#Formulaire de commentaire
class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']
        widgets = {
            'contenu': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre commentaire...'
                # 'rows': 4
            })
        }

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu', 'image', 'categories']
        widgets = {
            'titre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Titre de l\'article'
            }),
            'contenu': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Saisir votre texte ici .....',
                'rows': 7
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id': 'formFile'
            }),
            'categories': forms.Select(attrs={
                'class': 'form-control',
            })
        }
