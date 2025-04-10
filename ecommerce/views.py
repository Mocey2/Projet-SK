# ecommerce/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit, Panier, ArticlePanier, Client
from django.contrib.auth.decorators import login_required

def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'ecommerce/liste_produits.html', {'produits': produits})

def detail_produit(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    return render(request, 'ecommerce/detail_produit.html', {'produit': produit})

@login_required
def ajouter_au_panier(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    client, created = Client.objects.get_or_create(user=request.user)
    panier, created = Panier.objects.get_or_create(client=client)

    # Vérifier si l’article existe déjà dans le panier
    article_panier, created = ArticlePanier.objects.get_or_create(
        panier=panier,
        produit=produit
    )
    article_panier.quantite += 1
    article_panier.save()

    return redirect('ecommerce:detail_produit', produit_id=produit_id)

@login_required
def voir_panier(request):
    client, created = Client.objects.get_or_create(user=request.user)
    panier, created = Panier.objects.get_or_create(client=client)

    articles = ArticlePanier.objects.filter(panier=panier)
    total = sum([item.produit.prix * item.quantite for item in articles])

    return render(request, 'ecommerce/voir_panier.html', {
        'articles': articles,
        'total': total
    })

@login_required
def passer_commande(request):
    client, created = Client.objects.get_or_create(user=request.user)
    panier = client.panier
    articles = panier.articlepanier_set.all()

    if request.method == 'POST':
        # Création de la commande
        from .models import Commande, ArticleCommande

        commande = Commande.objects.create(client=client)
        for article in articles:
            ArticleCommande.objects.create(
                commande=commande,
                produit=article.produit,
                quantite=article.quantite,
                prix_unitaire=article.produit.prix
            )
        # Vider le panier
        articles.delete()
        return render(request, 'ecommerce/confirmation_commande.html', {'commande': commande})

    return render(request, 'ecommerce/passer_commande.html', {
        'articles': articles
    })
