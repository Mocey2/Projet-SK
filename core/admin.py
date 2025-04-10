from django.contrib import admin
from .models import Utilisateur, TokenAuthentification
from django.contrib.auth.admin import UserAdmin

@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    # Si tu veux personnaliser l’affichage
    fieldsets = (
        (None, {'fields': ('username', 'password', 'email', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')}),
    )

@admin.register(TokenAuthentification)
class TokenAuthentificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'token', 'date_creation')
