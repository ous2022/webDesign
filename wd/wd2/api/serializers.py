from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from wd2.models import *

from wd.views import connexion, inscription

# serializer pour la vue de connexion
class connexionSerializer(ModelSerializer):
    class Meta:
        #nom du modele
        model = Client
        fields = ['email','mot_de_passe']

# serializer pour la vue de connexion du prestataire
class prestataireSerializer(ModelSerializer):
    class Meta:
        #nom du modele
        model = Prestataire
        fields = ['email','mot_de_passe']

#serializer pour la vue de l'inscription
class inscriptionSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['nom_complet','mail_client','mot_de_passe','numero_de_telephone']
        extra_kwargs = {
            'mot_de_passe': {'write_only': True}  # Pour cacher le mot de passe à la lecture
        }


#serializer pour les articles dans le panier
class ArticlePanierSerializer(ModelSerializer):
    class Meta:
        model = ArticlePanier
        fields = ['panier','produit','quantite']

#serializzer pour l'ajout de produits
class ProduitSerializer(ModelSerializer):
    class Meta:
        model = Produit
        fields = ['nom','description','prix','categorie','image']

#serializer pour les categories
class CategorieSerializer(ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['nom','description']
    

    