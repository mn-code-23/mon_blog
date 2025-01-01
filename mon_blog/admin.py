from django.contrib import admin

from mon_blog.models import Article, Categorie, Commentaire

# Register your models here.

# Ajout des models
admin.site.register(Categorie)
admin.site.register(Article)
admin.site.register(Commentaire)

