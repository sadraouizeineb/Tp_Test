from django.shortcuts import render, get_object_or_404,redirect
from .models import Livre,Emprunt,Album
from .forms import LivreForm
from django.http import HttpResponse
from django.db.models import Avg,Count,F,Q
from django.utils import timezone
import datetime


def liste_livres(request):
    livres = Livre.objects.filter(disponible=True)
    return render(request, 'livres/liste_livres.html', {'livres': livres})

def liste_tout_livres(request):
    livres = Livre.objects.all
    return render(request, 'livres/liste_livres.html', {'livres': livres})



def detail_livre(request, livre_id):
    livre = get_object_or_404(Livre, id=livre_id)
    return render(request, 'livres/detail.html', {'livre': livre})


def ajouter_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_livres')
    else:
        form = LivreForm()
    return render(request, 'livres/ajouter_livre.html', {'form': form})

def update_livre(request, pk):
    livre = get_object_or_404(Livre, pk=pk)  
    if request.method == 'POST':
        form = LivreForm(request.POST, instance=livre) 
        if form.is_valid():
            form.save()
            return redirect('liste_livres')  
    else:
        form = LivreForm(instance=livre) 
    return render(request, 'livres/update_livre.html', {'form': form, 'livre': livre})


def livres_non_disponibles(request):
    livres = Livre.objects.filter(disponible=False)  
    return render(request, 'livres/livres_non_disponibles.html', {'livres': livres})


def emprunter_livre(request, livre_id):
    livre = get_object_or_404(Livre, id=livre_id)
    if livre.disponible:
        if request.method == 'POST':
            nom_emprunteur = request.POST.get('nom_emprunteur')
            if nom_emprunteur:
                # Créer un emprunt
                Emprunt.objects.create(livre=livre, nom_emprunteur=nom_emprunteur)
                # Mettre le livre à non disponible
                livre.disponible = False
                livre.save()
                return redirect('liste_livres')
            else:
                return HttpResponse("Le nom de l'emprunteur est requis.", status=400)
        return render(request, 'livres/emprunter_livre.html', {'livre': livre})
    else:
        return HttpResponse("Le livre n'est pas disponible.", status=400)


# ModelName.objects.all()[:10]  # Les 10 premiers objets

def fct(request):
    res = Album.objects.all()
    return render(request, "index.html", {"res": res})

# Récupérer tous les livres qui ne sont pas disponibles.
def livres_non_disponibles(request):
    livres = Livre.objects.exclude(disponible=True)
    return render(request, 'livres/livres_non_disponibless.html', {'livres': livres})

# Compter le nombre total de livres empruntés.

def count_emprunts(request):
    nombre_emprunts = Emprunt.objects.count()
    return render(request, 'livres/count_emprunts.html', {'nombre_emprunts': nombre_emprunts})

# Trier les livres par date de publication, du plus ancien au plus récent.



def livres_tries(request):
    livres = Livre.objects.order_by('date_publication')
    return render(request, 'livres/livres_tries.html', {'livres': livres})

# Vérifier si un livre avec un certain titre existe.

def livre_existe(request, titre):
    existe = Livre.objects.filter(titre=titre).exists()
    return render(request, 'livres/livre_exist.html', {'existe': existe})

# Créer un nouvel emprunt pour un livre.


def creer_emprunt(request):
    livre = Livre.objects.get(id=1)  # Par exemple, ID 1 pour le livre
    emprunt = Emprunt.objects.create(livre=livre, nom_emprunteur="Vithal")
    return render(request, 'livres/emprunt_cree.html', {'emprunt': emprunt})

# Mettre à jour tous les livres dont le titre contient "livre" pour les rendre indisponibles.


def update_livres_python(request):
    Livre.objects.filter(titre__icontains='livre').update(disponible=True)
    return render(request, 'livres/livres_update.html')



# Calculer la date moyenne de publication des livres.
def moyenne_date_publication(request):
    moyenne = Livre.objects.aggregate(Avg('date_publication'))
    return render(request, 'livres/moyenne_date_publication.html', {'moyenne': moyenne})


# Ajouter le nombre d'emprunts pour chaque livre.

def livres_avec_emprunts(request):
    livres = Livre.objects.annotate(nb_emprunts=Count('emprunt'))
    return render(request, 'livres/livres_avec_emprunts.html', {'livres': livres})

# Q - Filtrer les livres soit par auteur soit par disponibilité :



def livres_complexes(request):
    livres = Livre.objects.filter(Q(auteur='vithal') | Q(disponible=True))
    return render(request, 'livres/livres_complexes.html', {'livres': livres})






# vue qui récupère toutes les offres de livres (Livre) et, pour chaque livre, calcule :

# Le nombre total d'emprunts associés à chaque livre.
# La moyenne des emprunts acceptés ( des livres disponibles uniquement).
def livre_finale(request):
    livres = Livre.objects.annotate( nombre_emprunts=Count("livresEmprunté")).filter(disponible=True)  # Filtrer uniquement les livres disponibles

    for livre in livres:
        # Moyenne des dates d'emprunts pour les livres disponibles
        livre.moyenne_emprunts = Emprunt.objects.filter( livre__disponible=True).aggregate(moyenne_emprunts=Avg('livresEmprunté'))
   
    return render(request, 'livre_list.html', {'livres': livres})
