from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.shortcuts import redirect
from datetime import datetime
from .forms import ContactForm
from .forms import LivreForm
from librairie.models import Livre

def home(request):
    livres = Livre.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'librairie/accueil.html', {'derniers_livre': livres})
 
    
def view_article(request, id_article):
    """ 
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    return HttpResponse(
        "Vous avez demandé l'article n° {0} !".format(id_article)    
    )


def addition(request, nombre1, nombre2):    
    total = nombre1 + nombre2

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'librairie/addition.html', locals())
    


def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données 
        # que nous venons de récupérer
        envoi = True
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'librairie/contact.html', locals())
    
def livre(request):
    sauvegarde = False
 
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = LivreForm(request.POST or None, request.FILES)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid(): 
        livre=Livre()
        # Ici nous pouvons traiter les données du formulaire
        livre.titre = form.cleaned_data['titre']
        livre.auteur = form.cleaned_data['auteur']
        livre.resume = form.cleaned_data['resume']
        livre.date = form.cleaned_data['date']
        livre.photo = form.cleaned_data["photo"]
        sauvegarde = True

        # Nous pourrions ici envoyer l'e-mail grâce aux données 
        # que nous venons de récupérer
        
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'librairie/livre.html', {
        'form': form, 
        'sauvegarde': sauvegarde
    })

def livreDetails(request, id):
    try:
        livre = Livre.objects.get(id=id)
    except Livre.DoesNotExist:
        raise Http404

    return render(request, 'librairie/livreDetails.html', {'livre': livre})