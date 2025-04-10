from django.db import models
from django.conf import settings  # Pour accéder à AUTH_USER_MODEL

class Client(models.Model):
    """
    Dans ton diagramme, Client est lié à Utilisateur.
    On part du principe qu'un Client = 1 Utilisateur, 
    ou tu peux le décorréler si tu veux un compte client 
    distinct d’un compte staff par exemple.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='client_profile'
    )
    adresse = models.CharField(max_length=200, blank=True, null=True)
    ville = models.CharField(max_length=100, blank=True, null=True)
    pays = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"Client: {self.user.username}"


class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom_categorie


class Produit(models.Model):
    nom_produit = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, related_name='produits')
    # image = models.ImageField(upload_to='produits/', blank=True, null=True) # si tu veux gérer les images

    def __str__(self):
        return self.nom_produit


class Panier(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='panier')
    date_creation = models.DateTimeField(auto_now_add=True)
    # On peut lier directement un ManyToManyField via un intermédiaire
    produits = models.ManyToManyField(Produit, through='ArticlePanier')

    def __str__(self):
        return f"Panier de {self.client.user.username}"


class ArticlePanier(models.Model):
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantite} x {self.produit.nom_produit} dans le panier de {self.panier.client.user.username}"


class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='commandes')
    date_commande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=50, default='En cours')  # ex: "En cours", "Expédiée", "Livrée"

    def __str__(self):
        return f"Commande #{self.pk} de {self.client.user.username}"


class ArticleCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='articles_commandes')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantite} x {self.produit.nom_produit} (Commande #{self.commande.pk})"
