from django.db import models
from django.conf import settings

class ArticleBlog(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    date_publication = models.DateTimeField(auto_now_add=True)
    # Tu peux ajouter des catégories de blog, ou tags
    # categories = models.ManyToManyField('CategorieBlog', blank=True) # si tu veux

    def __str__(self):
        return self.titre


class Commentaire(models.Model):
    article = models.ForeignKey(ArticleBlog, on_delete=models.CASCADE, related_name='commentaires')
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_commentaire = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire par {self.auteur.username} sur {self.article.titre}"
