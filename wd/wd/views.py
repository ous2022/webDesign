from lib2to3.fixes.fix_input import context

from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import random
import string
from wd.forms import ConnexionForm,InscriptionForm,ProduitForm
from wd2.models import Client,Panier,ArticlePanier,Produit,Prestataire

# la vue pour a connexion
def connexion(request):
    if 'mail_clt' in request.session:#il s'est connecté), et  son e-mail a été stocké dans la session.
        return redirect('accueil')
    else:
        #verifier si la requête est post
        if request.method == 'POST':
            #recuperer le form de contact depuis la page
            form = ConnexionForm(request.POST)
            if form.is_valid(): #valider le form
                request.session['mail_clt'] = form.cleaned_data['mail_client']
                #recuperer  vers le profil

        #récuperer le form de connexion
        form = ConnexionForm()

        #passer le form de contact en parametres
        context = {'formCo': form}

        #afficher le template de page de co
        return render(request,'',context)



#la vue pour l'inscription
def inscription(request):
    if 'mail_clt' in request.session:
        return redirect('accueil')
    else:
        if request.method == 'POST':
            form = InscriptionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('connexion')

        form = InscriptionForm()
        context = {'formIns': form}
        return render(request,'',context)

# Déconnexion
def decoClient(request):
    try:
        # Supprime l'email de la session si présent
        if 'mailclt' in request.session:
            del request.session['mail_clt']
    except KeyError:
        pass

        # Redirige vers la page de connexion
    return redirect('connexion')

#vue pour ajouter un article dans le panier
def ajouter_au_panier(request, produit_id):
    if 'mail_clt' not in request.session:
        return redirect('connexion')  # Redirigez si l'utilisateur n'est pas connecté

    # Récupérer le client à partir de l'email stocké dans la session
    mail_client = request.session['mail_clt']
    client = get_object_or_404(Client, mail_client=mail_client)

    # Récupérer le produit par son id
    produit = get_object_or_404(Produit, id=produit_id)

    # Cherchez ou créez le panier pour ce client
    panier, created = Panier.objects.get_or_create(client=client)

    # Ajoutez un article au panier (vous pouvez adapter ce code selon votre structure de modèle)
    article_panier, created = ArticlePanier.objects.get_or_create(panier=panier, produit=produit)

    # Incrémentez la quantité si l'article est déjà dans le panier
    if not created:
        article_panier.quantite += 1
        article_panier.save()

    return redirect('panier')  # Redirigez vers la page du panier après ajout

#vue pour afficher les articles dans le panier
def afficher_panier(request):
    if 'mail_clt' not in request.session:
        return redirect('connexion')  # Redirigez vers la page de connexion si non connecté

    mail_client = request.session['mail_clt']
    client = get_object_or_404(Client, mail_client=mail_client)

    # Récupérez ou créez le panier du client
    panier, created = Panier.objects.get_or_create(client=client)

    # Récupérez tous les articles dans le panier
    articles_panier = panier.articlepanier_set.all()  # Utilisez votre relation pour récupérer les articles

    # Calculer le total si nécessaire
    total = sum(article.quantite * article.produit.prix for article in articles_panier)

    context = {
        'articles_panier': articles_panier,
        'total': total,
    }

    return render(request, 'panier.html', context)


# Vue pour ajouter un produit par le prestataire
def ajouter_produit(request):
    if 'prestataire_id' not in request.session:
        return redirect('connexion')  # Redirigez vers la page de connexion si le prestataire n'est pas connecté

    prestataire_id = request.session['prestataire_id']
    prestataire = get_object_or_404(Prestataire, id=prestataire_id)

    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)  # Assurez-vous de gérer les fichiers pour les images
        if form.is_valid():
            produit = form.save(commit=False)  # Ne pas enregistrer tout de suite
            produit.save()  # Sauvegarder le produit
            messages.success(request, "Produit ajouté avec succès.")
            return redirect('liste_produits')  # Redirigez vers une page de votre choix (ex: liste des produits)
    else:
        form = ProduitForm()

    context = {
        'form': form,
        'prestataire': prestataire,
    }
    return render(request, 'ajouter_produit.html', context)