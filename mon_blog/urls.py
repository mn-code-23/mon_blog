from django.conf.urls.static import static
from django.urls import path

from blog_personnel import settings
from mon_blog.views import index, detail, mes_publications, delete_AC, delete_Article, create_edit, edit_article

urlpatterns = [
    path('', index, name="index"),
    path('detail/<str:slug>/', detail, name="detail"),
    path('mes-publications/<str:username>/', mes_publications, name="mes_publications"),
    path('delcommentaire/<int:pk>/', delete_AC, name="delete_AC"),
    path('delarticle/<int:pk>/', delete_Article, name="delete_Article"),
    path('publier-article/', create_edit, name="create_edit"),
    path('edit-article/<int:pk>/', edit_article, name='edit_article'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)