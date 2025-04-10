from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    """
    Modèle utilisateur personnalisé si nécessaire.
    On peut ajouter des champs supplémentaires ici 
    (ex: téléphone, adresse, etc.)
    """
    # Champ téléphone
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    # Champ adresse
    adresse = models.TextField(blank=True, null=True)
    
    # Champ date de naissance
    date_naissance = models.DateField(blank=True, null=True)
    
    # Champ bio (description ou autres informations personnelles)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.username


class TokenAuthentification(models.Model):
    """
    Représentation d'un token d'authentification
    si on souhaite avoir un modèle custom.
    DRF, par défaut, a déjà un modèle Token.
    Mais on peut gérer manuellement s'il le faut.
    """
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='tokens')
    token = models.CharField(max_length=255, unique=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_expiration = models.DateTimeField(null=True, blank=True)  # Date d'expiration du token
    is_active = models.BooleanField(default=True)  # Le token est-il actif ?

    def __str__(self):
        return f"Token de {self.user.username} ({'actif' if self.is_active else 'inactif'})"
