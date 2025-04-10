# Generated by Django 5.2 on 2025-04-09 10:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_categorie', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.CharField(blank=True, max_length=200, null=True)),
                ('ville', models.CharField(blank=True, max_length=100, null=True)),
                ('pays', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_commande', models.DateTimeField(auto_now_add=True)),
                ('statut', models.CharField(default='En cours', max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commandes', to='ecommerce.client')),
            ],
        ),
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='panier', to='ecommerce.client')),
            ],
        ),
        migrations.CreateModel(
            name='ArticlePanier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField(default=1)),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('panier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.panier')),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_produit', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('categorie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='produits', to='ecommerce.categorie')),
            ],
        ),
        migrations.AddField(
            model_name='panier',
            name='produits',
            field=models.ManyToManyField(through='ecommerce.ArticlePanier', to='ecommerce.produit'),
        ),
        migrations.AddField(
            model_name='articlepanier',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.produit'),
        ),
        migrations.CreateModel(
            name='ArticleCommande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField(default=1)),
                ('prix_unitaire', models.DecimalField(decimal_places=2, max_digits=10)),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles_commandes', to='ecommerce.commande')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.produit')),
            ],
        ),
    ]
