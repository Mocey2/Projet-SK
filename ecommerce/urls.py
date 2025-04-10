from django.urls import path
from . import views

app_name = 'ecommerce'

urlpatterns = [
    path('produits/', views.liste_produits, name='liste_produits'),
    path('produits/<int:produit_id>/', views.detail_produit, name='detail_produit'),
    path('panier/ajouter/<int:produit_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('panier/', views.voir_panier, name='voir_panier'),
    path('commande/passer/', views.passer_commande, name='passer_commande'),
]
