from django.contrib import admin
from .models import Livre, Emprunt,Album

@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'disponible')
    list_filter = ('disponible',)

@admin.register(Emprunt)
class EmpruntAdmin(admin.ModelAdmin):
    list_display = ('livre', 'nom_emprunteur', 'date_emprunt')
admin.site.register(Album)