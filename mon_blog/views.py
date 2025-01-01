from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.text import slugify

from mon_blog.forms import CommentaireForm, CreateArticleForm
from mon_blog.models import Article, Commentaire, Categorie


# Create your views here.

#Vue index
def index(request):
    query = request.GET.get('q')  # Recuperation du mot cle de recherche
    category_id = request.GET.get('categorie')  #Recuperation de l'ID du categorie
    articles = Article.objects.all().order_by('-date_creation')

    #Filtrage par mot-cle
    if query:
        articles = articles.filter(titre__icontains=query)

    #Filtrage par categorie
    if category_id:
        articles = articles.filter(categories__id=category_id)

        # Ajoutez la pagination
    paginator = Paginator(articles, 8)  # 4 articles par page
    page_number = request.GET.get('page')  # Numéro de la page à afficher
    page_obj = paginator.get_page(page_number)  # Obtenez les articles de la page

    #Tous les categorie
    categories = Categorie.objects.all().order_by('-date_creation')

    return render(request, "mon_blog/index.html", context={"page_obj": page_obj,
                                                           "categories": categories})

# VUE DETAIL (VOIR PLUS)
def detail(request, slug):
    detail_article = get_object_or_404(Article, slug=slug)
    #Categories des articles
    categorie = detail_article.categories
    article_categorie = Article.objects.filter(categories=categorie)
    #les commentaire a afficher
    commentaires = Commentaire.objects.filter(article=detail_article).order_by('-date_creation')

    #Gestion du formulaire de commentaires
    if request.method == 'POST':
        form = CommentaireForm(request.POST)

        if form.is_valid():
            #creation du commentaire
            new_commentaire = form.save(commit=False)
            new_commentaire.article = detail_article
            new_commentaire.auteur = request.user
            new_commentaire.save()
            return redirect('detail', slug=slug)
    else:
        form = CommentaireForm()

    return render(request, "mon_blog/detail.html", context={"detail_article": detail_article,
                                                            "commentaires": commentaires,
                                                            "article_categorie": article_categorie,
                                                            "form": form})

# VUE Mes publications
def mes_publications(request, username):
    # Récupérer l'auteur
    User = get_user_model()
    auteur = get_object_or_404(User, username=username)

    # Récupérer tous les articles de cet auteur
    articles_auteur = Article.objects.filter(auteur=auteur).order_by('-date_creation')

    # Récupérer les détails d'un article spécifique et ses commentaires si un slug est présent
    mon_article = None
    mon_commentaires = None
    slug = request.GET.get('slug')
    if slug:
        mon_article = get_object_or_404(Article, slug=slug)
        mon_commentaires = Commentaire.objects.filter(article=mon_article).order_by('-date_creation')

    return render(request, "mon_blog/mes_publication.html", context={"auteur": auteur,
                                                                     "articles_auteur": articles_auteur,
                                                                     "mon_article": mon_article,
                                                                     "mon_commentaires": mon_commentaires,
                                                                     })

#VUE Suppression un commentaire
def delete_AC(request, pk):
    del_commentaire = get_object_or_404(Commentaire, pk=pk)
    del_commentaire.delete()
    # Rediriger vers la page précédente
    return redirect(request.META.get('HTTP_REFERER', '/'))

#VUE Suppression un article
def delete_Article(request, pk):
    del_article = get_object_or_404(Article, pk=pk)
    del_article.delete()
    # Rediriger vers la page précédente je rencontre des problemes de redirection sur la page
    return redirect('mes_publications', username=request.user.username)

#VUE Creer & Modifier un article
def create_edit(request):
    #Recuperer les articles de l'auteur
    articles_auteur = Article.objects.filter(auteur=request.user).order_by('-date_creation')

    # Gestion du formulaire des articles
    if request.method == 'POST':
        # Inclut les fichiers pour gérer les images
        form = CreateArticleForm(request.POST, request.FILES)

        if form.is_valid():
            print("Le formulaire est valide.")
            # creation du commentaire
            new_article = form.save(commit=False) # Ne sauvegarde pas immédiatement dans la base

            # Ajouter les champs non présents dans le formulaire
            new_article.auteur = request.user
            new_article.slug = slugify(new_article.titre) # Génère un slug à partir du titre

            new_article.save()
            print("Article enregistré.")
            # return redirect('create_edit')
            return redirect('index')
        else:
            print("Formulaire invalide :", form.errors)  # Affichez les erreurs du formulaire pour les comprendre
    else:
        form = CreateArticleForm()
    return render(request, "mon_blog/creer_article.html", context={"form": form,
                                                                    "articles_auteur": articles_auteur})

#VUE Modifier article
def edit_article(request, pk):
    # Recuperer les articles de l'auteur
    articles_auteur = Article.objects.filter(auteur=request.user).order_by('-date_creation')

    # Récupérer l'article à modifier
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        form = CreateArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirection après modification
    else:
        form = CreateArticleForm(instance=article)  # Charger les données existantes

    return render(request, 'mon_blog/edit_article.html', {'form': form,
                                                          'article': article,
                                                          'articles_auteur': articles_auteur})