from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.Home, name="bHome"),
    path('article/<int:article_id>/', views.Article, name="bArticle"),
    path('article/new/<int:profil_id>/', views.NewArticle, name="bNArticle"),
    path('article/search/', views.search, name="bSearch"),
    path('profil/<int:profil_id>/', views.Profile, name="bProfile"),
    path('accounts/signup/', views.signup, name="aSignup"),
    path('profil/settings/<int:profil_id>/', views.Parametres, name="bSettings")
]