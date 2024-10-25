from django.urls import path
from rest_framework.routers import DefaultRouter
from wd2.models import Client

from wd2.api.views import connexionVueSet,inscriptionVueSet,ArticlePanierVueSet,ProduitVueSet,prestataireVueSet,CategorieVueSet
#urls pour la connexion
connexion_router = DefaultRouter()
connexion_router.register(r'connexion', connexionVueSet)

#urls pour l'inscription
inscription_router = DefaultRouter()
inscription_router.register(r'inscription', inscriptionVueSet) #inscription(nom url)

#url pour les articles dans le panier
apanier_router = DefaultRouter()
apanier_router.register(r'apanier', ArticlePanierVueSet) 

#url pour l'ajout de produit
produit_router = DefaultRouter()
produit_router.register(r'produit', ProduitVueSet) 

#url pour la connexion prestataire
prestataire_router = DefaultRouter()
prestataire_router.register(r'prestataire', prestataireVueSet) 

#url pour la categorie
categorie_router = DefaultRouter()
categorie_router.register(r'categorie', CategorieVueSet) 