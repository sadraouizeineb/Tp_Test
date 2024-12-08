from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

# app_name = "livres" 
urlpatterns = [
    path('', views.liste_livres, name='liste_livres'),  # Liste des livres
    path('<int:livre_id>/', views.detail_livre, name='detail_livre'),  # Détails d'un livre
    path('ajouter/', views.ajouter_livre, name='ajouter_livre'),  # Ajouter un livre
    path('<int:pk>/update/', views.update_livre, name='update_livre'),  # Mise à jour
    path('non_disponibles/', views.livres_non_disponibles, name='livres_non_disponibles'),  # Nouvel URL
    path('<int:livre_id>/emprunter/', views.emprunter_livre, name='emprunter_livre'),  # Emprunter un livre
    # path('', views.liste_tout_livres, name='liste_tout_livres'),  # Liste des livres
  path('image/', views.fct, name='index'),  # Vue principale
#//////////////////////////
    path('livres/non_disponibles/', views.livres_non_disponibles, name='livres_non_disponibles'),
    path('count/emprunts/', views.count_emprunts, name='count_emprunts'),
    path('livres/tries/', views.livres_tries, name='livres_tries'),
    path('livre/existe/<str:titre>/', views.livre_existe, name='livre_existe'),
    path('emprunt/creer/', views.creer_emprunt, name='creer_emprunt'),
    path('livres/update/', views.update_livres_python, name='update_livres_python'),
    # path('moyenne/date_publication/', views.moyenne_date_publication, name='moyenne_date_publication'),
    path('livres/avec_emprunts/', views.livres_avec_emprunts, name='livres_avec_emprunts'),
    path('livres/complexes/', views.livres_complexes, name='livres_complexes'),
    path('livres/comparaison/', views.livres_comparaison, name='livres_comparaison'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)