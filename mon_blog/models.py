from django.db import models

# from blog_personnel import settings
from blog_personnel.settings import AUTH_USER_MODEL


# Create your models here.

# Model Categories
class Categorie(models.Model):
    name_categorie = models.CharField(max_length=200)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_categorie

# Model Article
class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    image = models.ImageField(upload_to="articles", blank=True, null=True)
    auteur = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    categories = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='categories')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

# Model Commentaire
class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commentaires')
    auteur = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article.titre
