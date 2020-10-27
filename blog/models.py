from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    NbArticles = models.IntegerField()
    Bio = models.TextField(max_length=300 ,null=True)

    def __str__(self):
        return self.User.username

class Article(models.Model):
    Auteur = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Titre = models.CharField(max_length=500)
    Image = models.URLField()
    Intro = models.TextField()

    def __str__(self):
        return self.Titre + " - " + self.Auteur.__str__()

class Paragraphe(models.Model):
    zArticle = models.ForeignKey(Article, on_delete=models.CASCADE)
    NumOrder = models.IntegerField()
    Content = models.TextField()
    Titre = models.CharField(max_length=200, null=True)

    def __str__(self):
        return "Paragraphe " + str(self.NumOrder) + " de l'article " + self.zArticle.__str__()
