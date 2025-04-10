from django.contrib import admin
from .models import (
    Client, Categorie, Produit, Panier, ArticlePanier, Commande, ArticleCommande
)

admin.site.register(Client)
admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Panier)
admin.site.register(ArticlePanier)
admin.site.register(Commande)
admin.site.register(ArticleCommande)
