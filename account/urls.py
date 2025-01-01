from django.conf.urls.static import static
from django.urls import path

from account.views import login_user, logout_user, singup_user, Mon_profil
from blog_personnel import settings

urlpatterns = [
    path('login/', login_user, name="login_user"),
    path('logout/', logout_user, name="logout_user"),
    path('singup/', singup_user, name="singup_user"),
    path('mon profil/<str:username>/', Mon_profil, name="Mon_profil"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)